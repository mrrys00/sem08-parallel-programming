#!/bin/bash
#SBATCH --job-name=test_job
#SBATCH --time=00:10:00
#SBATCH --account=plgmpr24-gpu-a100
#SBATCH --partition=plgrid-gpu-a100
#SBATCH --mem=40G
#SBATCH --gres=gpu:2

module load CUDA/12.2.0
python3 mnist.py
