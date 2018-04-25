# -*- coding: utf-8 -*-

import argparse

import nltk
from nltk.tokenize import word_tokenize

import utils


sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
class Tokenizer_with_nltk(object):
    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        for s in self.iterator:
            s = " ".join(s)
            all_tokens = []
            for s_i in sent_detector.tokenize(s):
                tokens = word_tokenize(s_i)
                all_tokens.extend(tokens)
            yield all_tokens

def run(path_in, path_out):
    # print("[nlppreprocess.tokenizer] Processing ...")
    iterator = utils.read_sentences(path_in)
    iterator = Tokenizer_with_nltk(iterator)
    utils.write_sentences(iterator, path_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input corpus", type=str, required=True)
    parser.add_argument("--output", help="path to output corpus", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output

    run(path_in=path_in, path_out=path_out)

