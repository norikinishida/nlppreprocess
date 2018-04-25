#!/usr/bin/env sh

INDIR=./data/raw
OUTDIR=./data/outdir

python make_filelist.py \
    --input ${INDIR}
./corenlp.sh ${OUTDIR}
python preprocess.py \
    --input ${INDIR} \
    --output ${OUTDIR}

