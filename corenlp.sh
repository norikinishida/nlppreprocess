#!/usr/bin/env sh

java edu.stanford.nlp.pipeline.StanfordCoreNLP \
    -annotators tokenize,ssplit \
    -outputFormat conll \
    -filelist ./filelist.txt \
    -outputDirectory $1
