#!/usr/bin/env sh

INPUT=/mnt/hdd/dataset/Book-Corpus/books_large.merge.head_50000.txt
TMP=./tmp.txt
OUTPUT=./books_large.merge.head_50000.txt.preprocessed

python lowercase.py \
    --input $INPUT \
    --output $TMP

# echo "[nlppreprocess;StanfordCoreNLP] Processing ..."
# rm tmp.properties
# touch tmp.properties
# echo "annotators = tokenize, ssplit" >> tmp.properties
# echo "ssplit.eolonly = true" >> tmp.properties
# echo "outputFormat = conll" >> tmp.properties
# echo "file = $TMP" >> tmp.properties
# java -Xmx10g edu.stanford.nlp.pipeline.StanfordCoreNLP -props tmp.properties
# python conll2lines.py \
#     --input $TMP.conll \
#     --output $TMP

python tokenizer.py \
    --input $TMP \
    --output $TMP \

python replace_digits.py \
    --input $TMP \
    --output $TMP

python append_eos.py \
    --input $TMP \
    --output $TMP

python replace_rare_words.py \
    --input $TMP \
    --output $OUTPUT \
    --prune_at 300000 \
    --min_count 5

python create_wordids.py \
    --corpus $OUTPUT
