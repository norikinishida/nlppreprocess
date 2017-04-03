#!/usr/bin/env sh

INPUT=./preprocess.py
OUTPUT=./output

python preprocess.py \
    --input $INPUT \
    --output $OUTPUT \
    --lowercase 1 \
    --replace_digits 1 \
    --append_eos 1 \
    --replace_rare 1 \
    --prune_at 1000000 \
    --min_count 0 

python create_wordids.py \
    --corpus $OUTPUT
