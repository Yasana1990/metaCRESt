#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

dir=`pwd`
cd $dir

while IFS=, read -r line1 line2 line3
do

fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files $line2

done < tableSRR.txt