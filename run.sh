#!/usr/bin/env sh

INPUT=/mnt/hdd/dataset/Book-Corpus/books_large.merge.head_50000.txt
TMP=./tmp.txt
OUTPUT=./books_large.merge.head_50000.txt.preprocessed

python lowercase.py \
    --input $INPUT \
    --output $TMP.lowercase

# echo "[nlppreprocess;StanfordCoreNLP] Processing ..."
# rm tmp.properties
# touch tmp.properties
# echo "annotators = tokenize, ssplit" >> tmp.properties
# echo "ssplit.eolonly = true" >> tmp.properties
# echo "outputFormat = conll" >> tmp.properties
# echo "file = $TMP.lowercase" >> tmp.properties
# java -Xmx10g edu.stanford.nlp.pipeline.StanfordCoreNLP -props tmp.properties
# python conll2lines.py \
#     --input $TMP.lowercase.conll \
#     --output $TMP.tokenize

python tokenizer.py \
    --input $TMP.lowercase \
    --output $TMP.tokenize

python replace_digits.py \
    --input $TMP.tokenize \
    --output $TMP.replace_digits

python append_eos.py \
    --input $TMP.replace_digits \
    --output $TMP.append_eos

python replace_rare_words.py \
    --input $TMP.append_eos \
    --output $OUTPUT \
    --prune_at 300000 \
    --min_count 0

python create_dictionary.py \
    --corpus $OUTPUT
