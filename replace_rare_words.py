# -*- coding: utf-8 -*-

import argparse

import gensim

import utils


def replace_rare_words(sents, prune_at, min_count):
    print "[nlppreprocess.replace_rare_words] Processing ..."

    # temporal dictionary
    dictionary = gensim.corpora.Dictionary(sents, prune_at=prune_at)
    dictionary.filter_extremes(no_below=min_count, no_above=1.0, keep_n=prune_at)
    vocab = dictionary.token2id
    print "[nlppreprocess.replace_rare_words] Vocabulary size: %d (w/o '<UNK>')" % len(vocab)

    identical = dict(zip(vocab, vocab))
    sents = [[identical.get(w, "<UNK>") for w in s] for s in sents]

    n_unk = 0
    n_total = 0
    for s in sents:
        for w in s:
            if w == "<UNK>":
                n_unk += 1
        n_total += len(s)
    print "[nlppreprocess.replace_rare_words] # of '<UNK>' tokens: %d (%d/%d = %.2f%%)" % \
            (n_unk, n_unk, n_total, float(n_unk)/n_total * 100)

    return sents


def main(path_in, path_out, prune_at, min_count):
    sents = utils.read_sentences(path_in)
    sents = replace_rare_words(sents, prune_at, min_count)
    utils.write_sentences(sents, path_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input corpus", type=str, required=True)
    parser.add_argument("--output", help="path to output corpus", type=str, required=True)
    parser.add_argument("--prune_at", help="prune at", type=int, default=1000000)
    parser.add_argument("--min_count", help="min count", type=int, default=0)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output
    prune_at = args.prune_at
    min_count = args.min_count

    main(path_in=path_in, path_out=path_out, prune_at=prune_at, min_count=min_count)
