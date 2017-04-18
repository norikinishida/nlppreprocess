# -*- coding: utf-8 -*-

import argparse
import os

import gensim

import utils


def main(path_corpus, path_dict, prune_at, min_count, char):
    assert os.path.exists(path_corpus)
    assert not os.path.exists(path_dict)
    
    assert path_dict.endswith(".dictionary")
    if char:
        print "[nlppreprocess.create_dictionary] NOTE: char-level mode!"
    
    iterator = utils.read_sentences(path_corpus, char=char)

    print "[nlppreprocess.create_dictionary] Processing ..."
    dictionary = gensim.corpora.Dictionary(iterator, prune_at=prune_at)
    print "[nlppreprocess.create_dictionary] Vocabulary size: %d (before filtering)" % len(dictionary.token2id)
    dictionary.filter_extremes(no_below=min_count, no_above=1.0, keep_n=prune_at)
    print "[nlppreprocess.create_dictionary] Vocabulary size: %d (after filtering)" % len(dictionary.token2id)
    
    dictionary.token2id["<UNK>"] = len(dictionary.token2id)
    print "[nlppreprocess.create_dictionary] Vocabulary size: %d (with '<UNK>')" % len(dictionary.token2id)
    
    dictionary.save_as_text(path_dict)
    print "[nlppreprocess.create_dictionary] Saved the dictionary to %s" % path_dict
   

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=str, required=True)
    parser.add_argument("--dict", type=str, required=True)
    parser.add_argument("--prune_at", type=int, default=1000000)
    parser.add_argument("--min_count", type=int, default=0)
    parser.add_argument("--char", type=int, default=0)
    args = parser.parse_args()

    path_corpus = args.corpus
    path_dict = args.dict
    prune_at = args.prune_at
    min_count = args.min_count
    char = bool(args.char)

    main(path_corpus=path_corpus, 
        path_dict=path_dict,
        prune_at=prune_at,
        min_count=min_count,
        char=char)
