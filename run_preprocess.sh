#!/usr/bin/env sh

INPUT=./preprocess.py
OUTPUT=./output

python preprocess.py \
    --input $INPUT \
    --output $OUTPUT \
    --lowercase True \
    --replace_digits True \
    --append_eos True \
    --replace_rare True \
    --prune_at 1000000 \
    --min_count 0 

python create_wordids.py \
    --corpus $OUTPUT
