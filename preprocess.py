# -*- coding: utf-8 -*-

import argparse
import os

import pyprind

import nlppreprocess.conll2lines
import nlppreprocess.lowercase
import nlppreprocess.replace_digits
import nlppreprocess.concat
import nlppreprocess.create_vocabulary
import nlppreprocess.replace_rare_words

N_TEST = 500

def main(args):
    path_root = args.path

    filenames = os.listdir(path_root)
    filenames = [n for n in filenames if n.endswith(".conll")]
    filenames.sort()

    for filename in pyprind.prog_bar(filenames):
        nlppreprocess.conll2lines.run(
            os.path.join(path_root, filename),
            os.path.join(path_root, filename + ".tokenized"))
        nlppreprocess.lowercase.run(
            os.path.join(path_root, filename + ".tokenized"),
            os.path.join(path_root, filename + ".tokenized.lowercased"))
        nlppreprocess.replace_digits.run(
            os.path.join(path_root, filename + ".tokenized.lowercased"),
            os.path.join(path_root, filename + ".tokenized.lowercased.replace_digits"))

    filepaths_train = [os.path.join(path_root, n + ".tokenized.lowercased.replace_digits") for n in filenames[:-N_TEST]]
    assert len(filepaths_train) == len(filenames) - N_TEST
    nlppreprocess.concat.run(
        filepaths_train,
        os.path.join(path_root, "concat.conll.tokenized.lowercased.replace_digits"))

    nlppreprocess.create_vocabulary.run(
        os.path.join(path_root, "concat.conll.tokenized.lowercased.replace_digits"),
        os.path.join(path_root, "vocab.txt"),
        prune_at=50000,
        min_count=5,
        special_words=[])

    filepaths_in = [os.path.join(path_root, n + ".tokenized.lowercased.replace_digits") for n in filenames]
    filepaths_out = [os.path.join(path_root, n + ".preprocessed") for n in filenames]
    nlppreprocess.replace_rare_words.run(
        filepaths_in,
        filepaths_out,
        path_vocab=os.path.join(path_root, "vocab.txt"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True)
    args = parser.parse_args()
    main(args)
