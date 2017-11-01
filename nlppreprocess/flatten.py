# -*- coding: utf-8 -*-

import argparse

import utils

def run(path_in, path_out):
    print("[nlppreprocess.flatten] Processing ...")
    print("[nlppreprocess.flatten] IN: %s" % path_in)
    print("[nlppreprocess.flatten] OUT : %s" % path_out)
    iterator = utils.read_sentences(path_in)
    with open(path_out, "w") as f:
        is_begin = True
        for s in iterator:
            for w in s:
                if is_begin:
                    f.write("%s" % w.encode("utf-8"))
                    is_begin = False
                else:
                    f.write(" %s" % w.encode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output

    run(path_in, path_out)
