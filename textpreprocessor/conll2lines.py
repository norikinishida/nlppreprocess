import argparse

from .iterators import write_sentences

def conll2lines(path_in):
    sentences = []
    buf = []
    for line in open(path_in):
        items = line.strip().split()
        if len(items) == 0:
            continue
        index = int(items[0])
        token = items[1]
        if index == 1:
            if len(buf) != 0:
                sentences.append(buf)
                buf = []
            else:
                pass
        buf.append(token)
    if len(buf) != 0:
        sentences.append(buf)
    return sentences

def run(path_in, path_out):
    sentences = conll2lines(path_in)
    write_sentences(sentences, path_out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output
    run(path_in=path_in, path_out=path_out)
