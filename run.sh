#!/usr/bin/env sh

RAW=/mnt/hdd/dataset/Book-Corpus/books_large.merge.head_50000.txt
CORPUS_TRAIN=./books_large.merge.head_50000.txt.preprocessed.train
CORPUS_VAL=./books_large.merge.head_50000.txt.preprocessed.val

python main.py \
    --raw $RAW \
    --train $CORPUS_TRAIN \
    --val $CORPUS_VAL

# echo "[nlppreprocess;StanfordCoreNLP] Processing ..."
# rm tmp.properties
# touch tmp.properties
# echo "annotators = tokenize, ssplit" >> tmp.properties
# echo "ssplit.eolonly = true" >> tmp.properties
# echo "outputFormat = conll" >> tmp.properties
# echo "file = $TMP.lowercase" >> tmp.properties
# java -Xmx10g edu.stanford.nlp.pipeline.StanfordCoreNLP -props tmp.properties
# python nlppreprocess/conll2lines.py \
#     --input $TMP.lowercase.conll \
#     --output $TMP.tokenize
