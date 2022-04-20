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

kallisto quant -i abundance/Trinity.index --single -o abundance/${line3}.Kal -l 52 -s 1 data/fastq/${line3}.fastq

done < data/tableSRR.txt




