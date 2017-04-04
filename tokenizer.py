# -*- coding: utf-8 -*-

import argparse

import nltk
from nltk.tokenize import word_tokenize

import utils


sent_detector = nltk.data.load("tokenizers/punkt/english.pickle")
def tokenize_with_nltk(sents):
    print "[nlppreprocess.tokenizer] Processing ..."
    sents = [" ".join(s) for s in sents] # back to original sentences
    def process(s):
        s = s.strip()
        all_words = []
        for s_i in sent_detector.tokenize(s):
            words = word_tokenize(s_i)
            all_words.extend(words)
        return all_words
    return [process(s) for s in sents]


def main(path_in, path_out):
    sents = utils.read_sentences(path_in)
    sents = tokenize_with_nltk(sents)
    utils.write_sentences(sents, path_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input corpus", type=str, required=True)
    parser.add_argument("--output", help="path to output corpus", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output

    main(path_in=path_in, path_out=path_out)

