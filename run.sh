#!/usr/bin/env sh

INDIR=/mnt/hdd/dataset/GutenbergDataset/Gutenberg/txt
OUTDIR=/mnt/hdd/projects/nlppreprocess/gutenberg

python nlppreprocess/make_filelist.py \
    --input_dir ${INDIR} \
    --output_dir ${OUTDIR} \
    --filelist_name filelist.txt \
    --end txt

./corenlp.sh ${OUTDIR}/filelist.txt ${OUTDIR}

python preprocess.py \
    --path ${OUTDIR}

