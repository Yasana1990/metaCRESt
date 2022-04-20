#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

mkdir genome

wget -O genome/Mus_musculus.GRCm39.dna.primary_assembly.fa.gz FILE http://ftp.ensembl.org/pub/release-105/fasta/mus_musculus/dna/Mus_musculus.GRCm39.dna.primary_assembly.fa.gz
gunzip genome/Mus_musculus.GRCm39.dna.primary_assembly.fa.gz
wget -O genome/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz FILE http://ftp.ensembl.org/pub/release-105/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz
gunzip genome/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz



