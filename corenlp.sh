#!/usr/bin/env sh

java -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP \
    -annotators tokenize,ssplit \
    -outputFormat conll \
    -filelist $1 \
    -outputDirectory $2

# if you need parse trees
# java -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP \
#     -annotators tokenize,ssplit,pos,lemma,depparse \
#     -outputFormat conll \
#     -filelist $1 \
#     -outputDirectory $2 \
#     -parse.originalDependencies


