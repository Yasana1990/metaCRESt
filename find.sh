#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

dir=`pwd`
cd $dir

dir=`pwd`
cd $dir

while IFS= read -r lineA
do
rm rawTPM_${lineA}.txt

while IFS=$'\t' read -r line1 line2 line3
do
grep ${line3} abundance/*.Kal/abundance.tsv >> rawTPM_${lineA}.txt
done < ContigID_${lineA}.txt

done < tdgfs_name.txt
