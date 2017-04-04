# -*- coding: utf-8 -*-

import argparse
import os

import gensim

import utils


def main(path):
    assert os.path.exists(path)

    sents = utils.read_sentences(path)

    # construct a dictionary
    print "[nlppreprocess.create_wordids] Processing ..."
    dictionary = gensim.corpora.Dictionary(sents, prune_at=None)
    vocab = dictionary.token2id
    print "[nlppreprocess.create_wordids] Vocabulary size: %d" % len(vocab)
    dictionary.save_as_text(path + ".dictionary")
    print "[nlppreprocess.create_wordids] Saved the dictionary to %s" % (path + ".dictionary")
    
    # transform to wordids
    sents = [[vocab[w] for w in s] for s in sents]

    # write
    sents = [[str(w) for w in s] for s in sents]
    utils.write_sentences(sents, path_out=path + ".wordids")
    print "[nlppreprocess.create_wordids] Wrote to %s" % (path + ".wordids")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=str, required=True)
    args = parser.parse_args()

    path = args.corpus

    main(path=path)
