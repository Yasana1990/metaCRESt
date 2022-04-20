#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

while IFS=, read -r line1 line2 line3
do
fastp -i fastq_1/${line3}_1-mus-hum.fastq -o fastq_1/${line3}_1-mus-hum-p.fastq --html fastq_1/${line3}_1-mus-hum-p.html -q 20 -u 30 -5 -3 -W 4 -M 20 -l 25
fastp -i fastq/${line3}-mus-hum.fastq -o fastq/${line3}-mus-hum-p.fastq --html fastq/${line3}-mus-hum-p.html -q 20 -u 30 -5 -3 -W 4 -M 20 -l 25
done < tableSRR.txt

#1>out.txt 2>err.txt
