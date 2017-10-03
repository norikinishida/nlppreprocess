# -*- coding: utf-8 -*-

import argparse

import utils


class ConvertTextlinesToChars(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for line in open(self.path):
            line = line.decode("utf-8")
            all_tokens = [self.transform(c) for c in line]
            yield all_tokens

    def transform(self, c):
        if c == " ":
            return "<SPACE>"
        elif c == "\n":
            return "<EOL>"
        else:
            return c

def run(path_in, path_out):
    print("[nlppreprocess.convert_textlines_to_characters] Processing ...")
    print("[nlppreprocess.convert_textlines_to_characters] IN: %s" % path_in)
    print("[nlppreprocess.convert_textlines_to_characters] OUT: %s" % path_out)
    iterator = ConvertTextlinesToChars(path_in)
    print("[nlppreprocess.convert_textlines_to_characters] Writing ...")
    utils.write_sentences(iterator, path_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path to input corpus", type=str, required=True)
    parser.add_argument("--output", help="path to output corpus", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output

    run(path_in=path_in, path_out=path_out)

