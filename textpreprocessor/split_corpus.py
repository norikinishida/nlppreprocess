import argparse

import numpy as np

from .iterators import read_sentences

def run(path_all, path_train, path_val, size):
    iterator = read_sentences(path_all)

    count = 0
    for s in open(path_all):
        count += 1
    N = count
    print("[textpreprocessor.split_corpus] Total size=%d" % N)

    perm = np.random.RandomState(1234).permutation(N)
    val_index = perm[-size:]

    f_train = open(path_train, "w")
    f_val = open(path_val, "w")
    for i, s in enumerate(iterator):
        line = " ".join(s)
        if i in val_index:
            f_val.write("%s\n" % line)
        else:
            f_train.write("%s\n" % line)
    f_train.flush()
    f_train.close()
    f_val.flush()
    f_val.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", type=str, required=True)
    parser.add_argument("--train", type=str, required=True)
    parser.add_argument("--val", type=str, required=True)
    parser.add_argument("--size", type=int, required=True)
    args = parser.parse_args()

    path_all = args.all
    path_train = args.train
    path_val = args.val
    size = args.size
    run(path_all=path_all, path_train=path_train, path_val=path_val, size=size)
