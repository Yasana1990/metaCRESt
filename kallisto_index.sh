#!/bin/bash

#SBATCH --mem 16GB
#SBATCH -p common
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 500:00:00

dir=`pwd`
cd $dir

kallisto index -i abundance/Trinity.index data/trinity_out_dir/Trinity.fasta
