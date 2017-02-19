#!/usr/bin/env sh

INPUT=/path/to/corpus
OUTPUT=./output

python preprocess.py \
    -i $INPUT \
    -o $OUTPUT 
