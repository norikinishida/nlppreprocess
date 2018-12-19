# -*- coding: utf-8 -*-


class WordIterator(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for s in open(self.path):
            yield s.strip().split()

def read_sentences(path_in):
    # f = open(path_in)
    # sents = [s.strip().split() for s in f]
    # return sents
    return WordIterator(path_in)

def write_sentences(iterator, path_out):
    with open(path_out, "w") as f:
        for s in iterator:
            line = " ".join(s)
            f.write("%s\n" % line)

