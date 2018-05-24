# -*- coding: utf-8 -*-

import argparse
import cPickle as pkl
import sys

import utils

class ReplaceRareWords(object):
    def __init__(self, iterator, vocab):
        self.iterator = iterator
        self.vocab = vocab

    def __iter__(self):
        for s in self.iterator:
            yield [w if w in self.vocab else "<UNK>" for w in s]

def count_UNK_rate(iterator):
    n_unk = 0
    n_total = 0
    for s in iterator:
        for w in s:
            if w == "<UNK>":
                n_unk += 1
        n_total += len(s)
    print "[nlppreprocess.replace_rare_words] # of '<UNK>' tokens=%d (%d/%d=%.2f%%)" % \
            (n_unk, n_unk, n_total, float(n_unk)/n_total * 100)

def run(path_in, path_out, path_vocab=None, vocab=None):
    # print("[nlppreprocess.replace_rare_words] Processing ...")
    if vocab is None:
        assert path_vocab.endswith("vocab")
        vocab = pkl.load(open(path_vocab, "rb"))
        vocab = set(vocab)
    else:
        assert isinstance(vocab, set)
    if isinstance(path_in, str) and isinstance(path_out, str):
        path_in_list = [path_in]
        path_out_list = [path_out]
    elif isinstance(path_in, unicode) and isinstance(path_out, unicode):
        path_in_list = [path_in]
        path_out_list = [path_out]
    elif isinstance(path_in, list) and isinstance(path_out, list):
        path_in_list = path_in
        path_out_list = path_out
    else:
        print("[nlppreprocess.replace_rare_words] Error: arguments path_in and path_out must be type of str or list.")
        sys.exit(-1) 
    assert len(path_in_list) == len(path_out_list)
    for path_in, path_out in zip(path_in_list, path_out_list):
        iterator = utils.read_sentences(path_in)
        iterator = ReplaceRareWords(iterator, vocab)
        # count_UNK_rate(iterator)
        utils.write_sentences(iterator, path_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--vocab", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output
    path_vocab = args.vocab

    run(path_in=path_in, path_out=path_out, path_vocab=path_vocab)
