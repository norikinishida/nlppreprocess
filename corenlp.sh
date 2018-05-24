#!/usr/bin/env sh

java edu.stanford.nlp.pipeline.StanfordCoreNLP \
    -annotators tokenize,ssplit \
    -outputFormat conll \
    -filelist $1 \
    -outputDirectory $2
