#!/bin/bash
# combineNunlComments.sh: combine duplicate files with different comments in downloads?/*
# usage: combineNunlComments.sh
# 20201004 erikt(at)xs4all.nl

BASEDIR="/home/erikt/projects/puregome/data/nunl"
OUTDIR="${BASEDIR}/downloads"
SCRIPT="../../scripts/combineNunlComments.py"

source activate python37
cd $BASEDIR
for ARTICLEID in `ls downloads?/*.csv|rev|cut -d- -f2|rev|sort -u|grep .......`
do
   OUTFILENAME="`ls downloads?/*-${ARTICLEID}-*|head -1|cut -d/ -f2-|sed 's/-[^-]*$//'`.csv"
   python3 $SCRIPT downloads?/*-${ARTICLEID}-* > $OUTDIR/$OUTFILENAME
   echo $OUTFILENAME
done
exit 0
