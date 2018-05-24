#!/usr/bin/env sh


# In this example, we use the Gutenberg Dataset that can be downloaded from ```https://web.eecs.umich.edu/~lahiri/gutenberg_dataset.html```
INDIR=/mnt/hdd/dataset/GutenbergDataset/Gutenberg/txt

# OUTDIR=/mnt/hdd/projects/nlppreprocess/gutenberg
OUTDIR=./data

python nlppreprocess/make_filelist.py \
    --input_dir ${INDIR} \
    --output_dir ${OUTDIR} \
    --filelist_name filelist.txt \
    --end txt

./corenlp.sh ${OUTDIR}/filelist.txt ${OUTDIR}

python preprocess.py \
    --path ${OUTDIR}

