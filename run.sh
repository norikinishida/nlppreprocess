#!/usr/bin/env sh

RAW=/mnt/hdd/dataset/Book-Corpus/books_large.merge.head_50000.txt
CORPUS_TRAIN=./books_large.merge.head_50000.txt.preprocessed.train
CORPUS_VAL=./books_large.merge.head_50000.txt.preprocessed.val

python template.py

# echo "[nlppreprocess;StanfordCoreNLP] Processing ..."
# rm tmp.properties
# touch tmp.properties
# echo "annotators = tokenize, ssplit" >> tmp.properties
# echo "ssplit.eolonly = true" >> tmp.properties
# echo "outputFormat = conll" >> tmp.properties
# echo "file = tmp.txt.lowercase" >> tmp.properties
# java -Xmx10g edu.stanford.nlp.pipeline.StanfordCoreNLP -props tmp.properties
# python nlppreprocess/conll2lines.py \
#     --input tmp.txt.lowercase.conll \
#     --output tmp.txt.lowercase.tokenize
