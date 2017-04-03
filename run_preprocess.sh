#!/usr/bin/env sh

INPUT=/mnt/hdd/dataset/Book-Corpus/books_large.merge.head_50000.txt
OUTPUT=./books_large.merge.head_50000.txt.preprocessed

python preprocess.py \
    --input $INPUT \
    --output $OUTPUT \
    --corenlp 1 \
    --lowercase 1 \
    --replace_digits 1 \
    --append_eos 1 \
    --replace_rare 1 \
    --prune_at 1000000 \
    --min_count 0 

python create_wordids.py \
    --corpus $OUTPUT
