#!/usr/bin/env sh

INPUT=./preprocess.py
OUTPUT=./output

python preprocess.py \
    --input $INPUT \
    --output $OUTPUT 

python create_wordids.py \
    --corpus $OUTPUT
