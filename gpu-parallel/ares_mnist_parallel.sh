#!/bin/bash
#SBATCH --job-name=v1_8_gpu
#SBATCH --output=%x_%j.out
#SBATCH --time=00:30:00
#SBATCH --partition=plgrid-gpu-v100
#SBATCH --account=plgmpr24-gpu
#SBATCH --mem=40G
#SBATCH --gres=gpu:8

module load tensorflow/2.8.0-fosscuda-2020b
python3 mnist.py