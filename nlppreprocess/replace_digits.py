# -*- coding: utf-8 -*-

import argparse
import re

import utils


class ReplaceDigits(object):
    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        for s in self.iterator:
            yield [re.sub(r"\d", "7", w) for w in s]

def run(path_in, path_out):
    print("[nlppreprocess.replace_digits] Processing ...")
    print("[nlppreprocess.replace_digits] IN: %s" % path_in)
    print("[nlppreprocess.replace_digits] OUT: %s" % path_out)
    iterator = utils.read_sentences(path_in)
    iterator = ReplaceDigits(iterator)
    print("[nlppreprocess.replace_digits] Writing ...")
    utils.write_sentences(iterator, path_out)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input corpus", type=str, required=True)
    parser.add_argument("--output", help="path to output corpus", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output

    run(path_in=path_in, path_out=path_out)
