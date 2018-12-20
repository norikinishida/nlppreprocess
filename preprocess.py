# -*- coding: utf-8 -*-

import argparse
import os

import pyprind

import textpreprocessor.conll2lines
import textpreprocessor.lowercase
import textpreprocessor.replace_digits
import textpreprocessor.concat
import textpreprocessor.create_vocabulary
import textpreprocessor.replace_rare_words

N_TEST = 500

def main(args):
    path_root = args.path

    filenames = os.listdir(path_root)
    filenames = [n for n in filenames if n.endswith(".conll")]
    filenames.sort()

    for filename in pyprind.prog_bar(filenames):
        textpreprocessor.conll2lines.run(
            os.path.join(path_root, filename),
            os.path.join(path_root, filename + ".tokenized"))
        textpreprocessor.lowercase.run(
            os.path.join(path_root, filename + ".tokenized"),
            os.path.join(path_root, filename + ".tokenized.lowercased"))
        textpreprocessor.replace_digits.run(
            os.path.join(path_root, filename + ".tokenized.lowercased"),
            os.path.join(path_root, filename + ".tokenized.lowercased.replace_digits"))

    filepaths_train = [os.path.join(path_root, n + ".tokenized.lowercased.replace_digits") for n in filenames[:-N_TEST]]
    assert len(filepaths_train) == len(filenames) - N_TEST
    textpreprocessor.concat.run(
        filepaths_train,
        os.path.join(path_root, "concat.conll.tokenized.lowercased.replace_digits"))

    textpreprocessor.create_vocabulary.run(
        os.path.join(path_root, "concat.conll.tokenized.lowercased.replace_digits"),
        os.path.join(path_root, "vocab.txt"),
        prune_at=50000,
        min_count=5,
        special_words=[])

    filepaths_in = [os.path.join(path_root, n + ".tokenized.lowercased.replace_digits") for n in filenames]
    filepaths_out = [os.path.join(path_root, n + ".preprocessed") for n in filenames]
    textpreprocessor.replace_rare_words.run(
        filepaths_in,
        filepaths_out,
        path_vocab=os.path.join(path_root, "vocab.txt"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, required=True)
    args = parser.parse_args()
    main(args)
