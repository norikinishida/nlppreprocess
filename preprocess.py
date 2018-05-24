# -*- coding: utf-8 -*-

import argparse
import os
import re

import nlppreprocess.conll2lines
import nlppreprocess.lowercase
import nlppreprocess.replace_digits
import nlppreprocess.concat
import nlppreprocess.create_vocabulary
import nlppreprocess.replace_rare_words

def aggregate_training_paths(filenames, path_outdir):
    re_comp = re.compile(r"^raw_([0-9]+)\.txt")
    result = []
    for filename in filenames:
        match = re_comp.findall(filename)
        assert len(match) == 1
        number = int(match[0])
        if 0 <= number <= 2:
            result.append(
                os.path.join(path_outdir, filename + ".tokenized.lowercased.replace_digits"))
    return result

def main(args):
    path_indir = args.input
    path_outdir = args.output

    filenames = os.listdir(path_indir)
    filenames = [n for n in filenames if n.startswith("raw_") and n.endswith(".txt")]

    for filename in filenames:
        nlppreprocess.conll2lines.run(
            os.path.join(path_outdir, filename + ".conll"),
            os.path.join(path_outdir, filename + ".tokenized"))
        nlppreprocess.lowercase.run(
            os.path.join(path_outdir, filename + ".tokenized"),
            os.path.join(path_outdir, filename + ".tokenized.lowercased"))
        nlppreprocess.replace_digits.run(
            os.path.join(path_outdir, filename + ".tokenized.lowercased"),
            os.path.join(path_outdir, filename + ".tokenized.lowercased.replace_digits"))

    filepaths_train = aggregate_training_paths(filenames, path_outdir)
    nlppreprocess.concat.run(
        filepaths_train,
        os.path.join(path_outdir, "concat.tokenized.lowercased.replace_digits"))

    nlppreprocess.create_vocabulary.run(
        os.path.join(path_outdir, "concat.tokenized.lowercased.replace_digits"),
        os.path.join(path_outdir, "vocab"),
        prune_at=1000000,
        min_count=2,
        special_words=[])

    filepaths_in = [os.path.join(path_outdir, n + ".tokenized.lowercased.replace_digits") for n in filenames]
    filepaths_out = [os.path.join(path_outdir, n + ".preprocessed") for n in filenames]
    nlppreprocess.replace_rare_words.run(
        filepaths_in,
        filepaths_out,
        path_vocab=os.path.join(path_outdir, "vocab"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()
    main(args)
