#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

dir=`pwd`
cd $dir
file="downloadSRR.txt"

while IFS=, read -r line1 line2
do
wget -c $line1
done < tableSRR.txt