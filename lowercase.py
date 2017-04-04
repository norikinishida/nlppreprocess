# -*- coding: utf-8 -*-

import argparse

import utils


def lowercase(sents):
    print "[nlppreprocess.lowercase] Processing ..."
    return [[w.lower() for w in s] for s in sents]


def main(path_in, path_out):
    sents = utils.read_sentences(path_in)
    sents = lowercase(sents)
    utils.write_sentences(sents, path_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input corpus", type=str, required=True)
    parser.add_argument("--output", help="path to output corpus", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output

    main(path_in=path_in, path_out=path_out)
