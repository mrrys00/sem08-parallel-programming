import tensorflow as tf

from time import time

# List all available GPUs
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("Available GPUs:")
    for gpu in gpus:
        print(gpu.name)
else:
    print("No GPUs available.")

# List all available CPUs
gpus = tf.config.list_physical_devices('CPU')
if gpus:
    print("Available CPUs:")
    for gpu in gpus:
        print(gpu)
else:
    print("No CPUs available.")