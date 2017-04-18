# -*- coding: utf-8 -*-

import argparse

import gensim

import utils


class ReplaceRareWords(object):
    def __init__(self, iterator, dictionary, char):
        self.iterator = iterator
        self.vocab = dictionary.token2id
        if not char:
            self.UNK = "<UNK>"
        else:
            self.UNK = "0"

    def __iter__(self):
        identical = dict(zip(self.vocab, self.vocab))
        for s in self.iterator:
            yield [identical.get(w, self.UNK) for w in s]


def count_UNK_rate(iterator):
    n_unk = 0
    n_total = 0
    for s in iterator:
        for w in s:
            if w == "<UNK>":
                n_unk += 1
        n_total += len(s)
    print "[nlppreprocess.replace_rare_words] # of '<UNK>' tokens: %d (%d/%d = %.2f%%)" % \
            (n_unk, n_unk, n_total, float(n_unk)/n_total * 100)


def main(path_in, path_out, path_dict, char):
    assert path_dict.endswith(".dictionary")
    if char:
        print "[nlppreprocess.replace_rare_words] NOTE: char-level mode!"

    print "[nlppreprocess.replace_rare_words] Processing ..."
    dictionary = gensim.corpora.Dictionary.load_from_text(path_dict)

    iterator = utils.read_sentences(path_in, char=char)

    iterator = ReplaceRareWords(iterator, dictionary, char=char)

    count_UNK_rate(iterator)

    utils.write_sentences(iterator, path_out, char=char)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True)
    parser.add_argument("--output", type=str, required=True)
    parser.add_argument("--dict", type=str, required=True)
    parser.add_argument("--char", type=int, default=0)
    args = parser.parse_args()

    path_in = args.input
    path_out = args.output
    path_dict = args.dict
    char = bool(args.char)

    main(path_in=path_in, path_out=path_out, path_dict=path_dict, char=char)
