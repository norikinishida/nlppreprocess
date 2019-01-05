import argparse

from .iterators import write_sentences

class ConvertTextlinesToChars(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        for line in open(self.path):
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
    iterator = ConvertTextlinesToChars(path_in)
    write_sentences(iterator, path_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output
    run(path_in=path_in, path_out=path_out)

