#!/usr/bin/env sh

INDIR=./data/raw
OUTDIR=./data/outdir

python nlppreprocess/make_filelist.py \
    --input_dir ${INDIR} \
    --output_dir ${OUTDIR} \
    --filelist_name filelist.txt \
    --begin raw \
    --end txt
./corenlp.sh ${OUTDIR}/filelist.txt ${OUTDIR}
python preprocess.py \
    --input ${INDIR} \
    --output ${OUTDIR}

