# -*- coding: utf-8 -*-

"""
入力されるコーパスは, 1行に1文ずつ記述されていること.
"""

import argparse
import os
import re

import gensim
import nltk
from nltk.tokenize import word_tokenize
from stream import *

from generators import StartGenerator, FakeGenerator, ChainGenerator


def load_sentences(path):
    sents = StartGenerator(path)
    sents = FakeGenerator(sents,
            lambda sents_: sents_ >> map(lambda s: s.decode("utf-8")))
    return sents


sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
def tokenize(s):
    words = []
    s = s.strip()
    for s_i in sent_detector.tokenize(s):
        words_i = word_tokenize(s_i)
        words.extend(words_i)
    return words


def replace_words_with_UNK(sents, vocab, UNK):
    identical = dict(zip(vocab, vocab))
    return FakeGenerator(sents,
            lambda sents_: sents_ >> map(lambda s: [identical.get(w, "<UNK>") for w in s]))


def preprocess_sentences(
        sents,
        lowercase,
        replace_digits,
        append_eos,
        replace_rare, prune_at=-1, min_count=-1):

    print "[info] LOWERCASE?: %s" % lowercase
    print "[info] REPLACE DIGITS?: %s" % replace_digits
    print "[info] APPEND '<EOS>'?: %s" % append_eos
    print "[info] REPLACE RARE WORDS?: %s" % replace_rare
    print "[info] PRUNE AT: %s" % prune_at
    print "[info] MINIMUM COUNT: %s" % min_count

    if replace_rare:
        assert prune_at >= 0
        assert min_count >= 0

    # (1) Tokenizing
    sents = FakeGenerator(sents,
            lambda sents_: sents_
                >> map(lambda s: tokenize(s))
                >> filter(lambda s: len(s) != 0))
    
    # (2) Converting words to lower case
    if lowercase:
        sents = FakeGenerator(sents,
            lambda sents_: sents_ 
                >> map(lambda s: [w.lower() for w in s]))

    # (3) Replacing digits with '7'
    if replace_digits:
        sents = FakeGenerator(sents,
            lambda sents_: sents_
                >> map(lambda s: [re.sub(r"\d", "7", w) for w in s]))

    # (4) Appending '<EOS>' tokens for each sentence
    if append_eos:
        sents = FakeGenerator(sents,
            lambda sents_: sents_
                >> map(lambda s: s + ["<EOS>"]))

    # (5) Replacing rare words with '<UNK>' tokens
    if replace_rare:
        # temporal dictionary
        dictionary = gensim.corpora.Dictionary(sents, prune_at=prune_at)
        dictionary.filter_extremes(no_below=min_count, no_above=1.0, keep_n=prune_at)
        print "[info] Vocabulary size: %d (w/o '<UNK>')" % len(dictionary.token2id)

        sents = replace_words_with_UNK(sents, dictionary.token2id, "<UNK>")

        n_unk = 0
        n_total = 0
        for s in sents:
            for w in s:
                if w == "<UNK>":
                    n_unk += 1
            n_total += len(s)
        print "[info] # of '<UNK>' tokens: %d (%d/%d = %.2f%%)" % \
            (n_unk, n_unk, n_total, float(n_unk)/n_total*100)
    
    return list(sents)


def write_sentences(sents, path):
    with open(path, "w") as f:
        for s in sents:
            line = " ".join(s).encode("utf-8") + "\n"
            f.write(line)


def main(
        path_in, path_out,
        lowercase,
        replace_digits,
        append_eos, 
        replace_rare, prune_at, min_count):
    assert os.path.exists(path_in)
    assert os.path.exists(os.path.dirname(path_out))

    print "[info] INPUT: %s" % path_in
    print "[info] OUTPUT: %s" % path_out

    sents = load_sentences(path=path_in)

    sents = preprocess_sentences(
            sents,
            lowercase=lowercase,
            replace_digits=replace_digits,
            append_eos=append_eos,
            replace_rare=replace_rare,
            prune_at=prune_at,
            min_count=min_count)

    write_sentences(sents, path=path_out)
    print "[info] Wrote to %s" %  path_out

    print "[info] Done."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input corpus", type=str, required=True)
    parser.add_argument("--output", help="path to output corpus", type=str, required=True)
    parser.add_argument("--lowercase", help="lowercase?", type=int, default=True)
    parser.add_argument("--replace_digits", help="replace digits?", type=int, default=True)
    parser.add_argument("--append_eos", help="append '<EOS>' tokens?", type=int, default=True)
    parser.add_argument("--replace_rare", help="replace rare words?", type=int, default=True)
    parser.add_argument("--prune_at", help="prune_at", type=int, default=1000000)
    parser.add_argument("--min_count", help="min_count", type=int, default=0)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output
    lowercase = bool(args.lowercase)
    replace_digits = bool(args.replace_digits)
    append_eos = bool(args.append_eos)
    replace_rare = bool(args.replace_rare)
    prune_at = args.prune_at
    min_count = args.min_count

    main(
        path_in=path_in,
        path_out=path_out,
        lowercase=lowercase,
        replace_digits=replace_digits,
        append_eos=append_eos,
        replace_rare=replace_rare,
        prune_at=prune_at,
        min_count=min_count)
