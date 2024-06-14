"""
Source: https://hpc.nmsu.edu/discovery/software/tensorflow/using-tensorflow/
"""

import tensorflow as tf

from time import time


# List all available GPUs
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("Available GPUs:")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPUs available.")
    
gpus = tf.config.list_physical_devices('CPU')
if gpus:
    print("Available CPUs:")
    for gpu in gpus:
        print(gpu)
else:
    print("No CPUs available.")
    
## 

mnist = tf.keras.datasets.mnist
mnist = tf.keras.datasets.mnist

start_time = time()

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])
predictions = model(x_train[:1]).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

model.compile(
    optimizer='adam',
    loss=loss_fn,
    metrics=['accuracy'])
model.fit(x_train, y_train, epochs=50)
model.evaluate(x_test,  y_test, verbose=2)

print(f"full time {time() - start_time}")
