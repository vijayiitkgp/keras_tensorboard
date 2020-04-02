from time import time
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import TensorBoard, ReduceLROnPlateau
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.utils import plot_model
# from ann_visualizer.visualize import ann_viz


import os
path_var = r"C:/Program Files (x86)/Graphviz2.38/bin/"
os.environ["PATH"] += os.pathsep + path_var
#C:\Program Files (x86)\Graphviz2.38\bin

fashion_mnist = fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = Sequential()
# model.add(Dense(80, input_shape=(4,), activation='sigmoid'))

model.add(keras.layers.Flatten(input_shape=(28, 28)))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(10, activation=tf.nn.softmax))



model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                            #   patience=5, min_lr=0.001)
tensorboard = TensorBoard(log_dir="logs/{}".format(time()))
#plot_model(model, to_file='model.png')	
plot_model(model, to_file='model.png', show_shapes = True, show_layer_names = True)	


# ann_viz(model, title="My first neural network", view= False, filename = "keras_model" )	  
model.fit(train_images, train_labels, epochs=200, verbose=1, callbacks=[tensorboard])
