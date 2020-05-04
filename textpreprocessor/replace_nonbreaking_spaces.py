import argparse
import re

from .iterators import read_sentences, write_sentences

class ReplaceNonBreakingSpace(object):
    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        for s in self.iterator:
            yield [x for w in s for x in w.replace("\xa0", " ").split()]

def run(path_in, path_out):
    iterator = read_sentences(path_in)
    iterator = ReplaceNonBreakingSpace(iterator)
    write_sentences(iterator, path_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output
    run(path_in=path_in, path_out=path_out)
