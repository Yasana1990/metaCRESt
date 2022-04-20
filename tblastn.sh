#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

dir=`pwd`
cd $dir

while IFS= read -r line1
do

tblastn -query data/TDGFs/${line1} -subject data/trinity_out_dir/Trinity.fasta > tblastn_${line1}

done < tdgfs_name.txt