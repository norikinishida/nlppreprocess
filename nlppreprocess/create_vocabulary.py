# -*- coding: utf-8 -*-

import argparse
from collections import Counter, OrderedDict
import cPickle as pkl
import os

import utils


def run(path_corpus, path_vocab, prune_at, min_count, special_words):
    assert os.path.exists(path_corpus)
    assert not os.path.exists(path_vocab)
    assert path_vocab.endswith(".vocab")

    print("[nlppreprocess.create_vocabulary] Processing ...")
    print("[nlppreprocess.create_vocabulary] INPUT CORPUS: %s" % path_corpus)
    print("[nlppreprocess.create_vocabulary] OUTPUT VOCABULARY: %s" % path_vocab)
    print("[nlppreprocess.create_vocabulary] PRUNE AT: %d" % prune_at)
    print("[nlppreprocess.create_vocabulary] MINIMUM COUNT: %d" % min_count)
    print("[nlppreprocess.create_vocabulary] SPECIAL WORDS: %s" % special_words)

    iterator = utils.read_sentences(path_corpus)
    counter = Counter()
    for s in iterator:
        counter.update(s)
    counter = counter.most_common()[:prune_at]
    frequencies = dict(counter)
    counter.sort(key=lambda x: (-x[1], x[0]))
    vocab_words = [w for w,freq in counter if freq >= min_count]
    for sw in special_words:
        if not sw in vocab_words:
            vocab_words = vocab_words + [sw]
            frequencies[sw] = 0 # TODO
    vocab = OrderedDict()
    for w_id, w in enumerate(vocab_words):
        vocab[w] = w_id
    if not "<UNK>" in vocab.keys():
        vocab["<UNK>"] = len(vocab)
        frequencies["<UNK>"] = 0 # TODO
    print("[nlppreprocess.create_vocabulary] Vocabulary size (w/ '<UNK>'): %d" % len(vocab))
    
    pkl.dump(vocab, open(path_vocab, "wb"))
    print("[nlppreprocess.create_vocabulary] Saved the vocabulary (pickle) to %s" % path_vocab)
    with open(path_vocab + ".txt", "w") as f:
        for w, w_id in vocab.items():
            freq = frequencies[w]
            f.write("%s\t%d\t%d\n" % (w.encode("utf-8"), w_id, freq))
    print("[nlppreprocess.create_vocabulary] Saved the vocabulary (text) to %s" % (path_vocab + ".txt"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=str, required=True)
    parser.add_argument("--vocab", type=str, required=True)
    parser.add_argument("--prune_at", type=int, default=1000000)
    parser.add_argument("--min_count", type=int, default=0)
    parser.add_argument("--special", type=str, nargs="+", default=[])
    args = parser.parse_args()

    path_corpus = args.corpus
    path_vocab = args.vocab
    prune_at = args.prune_at
    min_count = args.min_count
    special_words = args.special

    run(path_corpus=path_corpus, 
        path_vocab=path_vocab,
        prune_at=prune_at,
        min_count=min_count,
        special_words=special_words)
