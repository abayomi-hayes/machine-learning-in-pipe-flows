# -*- coding: utf-8 -*-
"""machine learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1flkgXKVana1-gIms8a-44oWc7SV9oxdZ
"""

import tensorflow as tf
import numpy as np

celcius_q = np.array([-40,-10,0,8,15,22,38])
fahenrite_a = np.array([-40,14,32,46,59,72,100])
for i,c in enumerate(celcius_q):
   print("{} the degree celcius_q = {} degree Fahenrite".format(c,fahenrite_a[i]))

machine_learning_model = tf.keras.layers.Dense(units=1, input_shape = [1])
model = tf.keras.Sequential([machine_learning_model])
model.compile(loss = "mean_squared_error",
              optimizer=tf.keras.optimizers.Adam(0.1))

history = model.fit(celcius_q,fahenrite_a, epochs=500, verbose=False)
print("finished training the model")

print(model.predict([100]))