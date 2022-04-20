#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p general
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

while IFS=, read -r line1 line2 line3
do
bowtie2 -x genome/index-mus -U fastq_1/${line3}_1.fastq --un fastq_1/${line3}_1-mus.fastq
bowtie2 -x genome/index-hum -U fastq_1/${line3}_1-mus.fastq --un fastq_1/${line3}_1-mus-hum.fastq

bowtie2 -x genome/index-mus -U fastq/${line3}.fastq --un fastq/${line3}-mus.fastq
bowtie2 -x genome/index-hum -U fastq/${line3}-mus.fastq --un fastq/${line3}-mus-hum.fastq

done < tableSRR.txt

#1>out.txt 2>err.txt
