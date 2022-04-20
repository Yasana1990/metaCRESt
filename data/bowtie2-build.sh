#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p general
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

bowtie2-build genome/Homo_sapiens.GRCh38.dna.primary_assembly.fa index-hum 
bowtie2-build genome/Mus_musculus.GRCm39.dna.primary_assembly.fa index-mus

#1>out.txt 2>err.txt
