# -*- coding: utf-8 -*-

import nlppreprocess.lowercase
import nlppreprocess.tokenizer
import nlppreprocess.convert_textlines_to_characters
import nlppreprocess.replace_digits
import nlppreprocess.append_eos
import nlppreprocess.split_corpus
import nlppreprocess.create_dictionary
import nlppreprocess.replace_rare_words


# RAW_CORPUS = "/path/to/raw_corpus"
# TRAIN_CORPUS = "/path/to/training_corpus"
# VAL_CORPUS = "/path/to/validation_corpus"
RAW_CORPUS = "/mnt/hdd/dataset/Book-Corpus/books_large.merge.head_50000.txt"
TRAIN_CORPUS = "./books_large.merge.head_50000.txt.preprocessed.train"
VAL_CORPUS = "./books_large.merge.head_50000.txt.preprocessed.val"

def main():
    tmp = "tmp.txt"
    nlppreprocess.lowercase.run(
            RAW_CORPUS,
            tmp + ".lowercase")
    nlppreprocess.tokenizer.run(
            tmp + ".lowercase",
            tmp + ".lowercase.tokenize")
    # nlppreprocess.convert_textlines_to_characters.run(
    #         tmp + ".lowercase.tokenize",
    #         tmp + ".lowercase.tokenize.char")
    nlppreprocess.replace_digits.run(
            tmp + ".lowercase.tokenize",
            tmp + ".lowercase.tokenize.replace_digits")
    nlppreprocess.append_eos.run(
            tmp + ".lowercase.tokenize.replace_digits",
            tmp + ".lowercase.tokenize.replace_digits.append_eos")
    nlppreprocess.split_corpus.run(
            tmp + ".lowercase.tokenize.replace_digits.append_eos",
            tmp + ".lowercase.tokenize.replace_digits.append_eos.train",
            tmp + ".lowercase.tokenize.replace_digits.append_eos.val",
            size=5000)
    nlppreprocess.create_dictionary.run(
            tmp + ".lowercase.tokenize.replace_digits.append_eos.train",
            TRAIN_CORPUS + ".dictionary",
            prune_at=300000,
            min_count=5)
    nlppreprocess.replace_rare_words.run(
            tmp + ".lowercase.tokenize.replace_digits.append_eos.train",
            TRAIN_CORPUS,
            path_dict=TRAIN_CORPUS + ".dictionary")
    nlppreprocess.replace_rare_words.run(
            tmp + ".lowercase.tokenize.replace_digits.append_eos.val",
            VAL_CORPUS,
            path_dict=TRAIN_CORPUS + ".dictionary")


if __name__ == "__main__":
    main()
