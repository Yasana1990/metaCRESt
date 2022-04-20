#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

dir=`pwd`
cd $dir

mkdir fastq
mkdir fastq_1

while IFS=, read -r line1 line2 line3
do
mv ${line2}.fastq fastq/${line3}.fastq
mv ${line2}_1.fastq fastq_1/${line3}_1.fastq
done < tableSRR.txt