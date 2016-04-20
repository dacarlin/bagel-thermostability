#!/bin/sh
#SBATCH --job-name=ddg
#SBATCH --output=log.txt 

MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
srun /share/work/rosetta/source/bin/ddg_monomer.linuxgccrelease @flags -resfile resfiles/$MUT
