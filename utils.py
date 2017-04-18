# -*- coding: utf-8 -*-


class WordIterator(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for s in open(self.path):
            yield s.decode("utf-8").strip().split()


class CharIterator(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for s in open(self.path):
            yield list(s.decode("utf-8").replace("\n", "\\"))


def read_sentences(path_in, char=False):
    # f = open(path_in)
    # sents = [s.decode("utf-8").strip().split() for s in f]
    # return sents
    if not char:
        return WordIterator(path_in)
    else:
        return CharIterator(path_in)


def write_sentences(iterator, path_out, char=False):
    print "[nlppreprocess.utils] Writing ..."
    with open(path_out, "w") as f:
        for s in iterator:
            if not char:
                line = " ".join(s)
            else:
                line = "".join(s)
            f.write("%s\n" % line.encode("utf-8"))
