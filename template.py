# -*- coding: utf-8 -*-

import nlppreprocess.lowercase
import nlppreprocess.tokenizer
import nlppreprocess.convert_textlines_to_characters
import nlppreprocess.replace_digits
import nlppreprocess.append_eos
import nlppreprocess.split_corpus
import nlppreprocess.create_vocabulary
import nlppreprocess.replace_rare_words


INPUT_CORPUS = "/path/to/raw_corpus"
OUTPUT_CORPUS_TRAIN = "/path/to/training_corpus"
OUTPUT_CORPUS_VAL = "/path/to/validation_corpus"
# INPUT_CORPUS = "/mnt/hdd/dataset/Book-Corpus/books_large.merge.head_50000.txt"
# OUTPUT_CORPUS_TRAIN = "./books_large.merge.head_50000.txt.preprocessed.train"
# OUTPUT_CORPUS_VAL = "./books_large.merge.head_50000.txt.preprocessed.val"

def main():
    tmp = "tmp.txt"
    nlppreprocess.lowercase.run(
            INPUT_CORPUS,
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
    nlppreprocess.create_vocabulary.run(
            tmp + ".lowercase.tokenize.replace_digits.append_eos.train",
            OUTPUT_CORPUS_TRAIN + ".vocab",
            prune_at=300000,
            min_count=5,
            special_words=["<EOS>"])
    nlppreprocess.replace_rare_words.run(
            tmp + ".lowercase.tokenize.replace_digits.append_eos.train",
            OUTPUT_CORPUS_TRAIN,
            path_vocab=OUTPUT_CORPUS_TRAIN + ".vocab")
    nlppreprocess.replace_rare_words.run(
            tmp + ".lowercase.tokenize.replace_digits.append_eos.val",
            OUTPUT_CORPUS_VAL,
            path_vocab=OUTPUT_CORPUS_TRAIN + ".vocab")


if __name__ == "__main__":
    main()
