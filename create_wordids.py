# -*- coding: utf-8 -*-

import argparse
import os

import gensim
from stream import *

from preprocess import load_sentences, write_sentences
from generators import FakeGenerator


def main(path):
    assert os.path.exists(path)

    sents = load_sentences(path)

    # split
    sents = FakeGenerator(sents,
            lambda sents_: sents_
                >> map(lambda s: s.split()))
    
    # construct a dictionary
    dictionary = gensim.corpora.Dictionary(sents, prune_at=None)
    vocab = dictionary.token2id
    # ivocab = {i:w for w,i in vocab.items()}
    print "Vocabulary size: %d" % len(vocab)
    dictionary.save_as_text(path + ".dictionary")
    print "Saved the dictionary to %s" % (path + ".dictionary")
    
    # transform to wordids
    sents = FakeGenerator(sents,
            lambda sents_: sents_
                >> map(lambda s: [vocab[w] for w in s]))

    # write
    sents = FakeGenerator(sents,
            lambda sents_: sents_
                >> map(lambda s: [str(w) for w in s]))
    write_sentences(sents, path=path + ".wordids")
    print "Wrote to %s" % (path + ".wordids")

    print "Done."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=str, required=True)
    args = parser.parse_args()

    path = args.corpus

    main(path=path)
