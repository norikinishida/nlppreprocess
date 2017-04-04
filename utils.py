# -*- coding: utf-8 -*-


def read_sentences(path_in):
    f = open(path_in)
    sents = [s.decode("utf-8").strip().split() for s in f]
    return sents


def write_sentences(sents, path_out):
    with open(path_out, "w") as f:
        for s in sents:
            line = " ".join(s)
            f.write("%s\n" % line.encode("utf-8"))
