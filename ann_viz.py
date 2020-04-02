import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, Activation
import json

network = Sequential();


def build_cnn_model():
  model = keras.models.Sequential()

  model.add(Dense(80, input_shape=(4,)));
  model.add(Activation('sigmoid'));
  model.add(Dense(60));
  model.add(Activation('sigmoid'));
  model.add(Dense(1));

  return model

network = build_cnn_model();

from ann_visualizer.visualize import ann_viz

ann_viz(network, title="", view=True);

print(network.layers[1].get_config());