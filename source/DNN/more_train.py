import numpy as np
import tensorflow as tf
import keras
import matplotlib.pyplot as plt
import time, os
from keras.models import Model, load_model
from keras import optimizers, initializers, losses
from keras.utils.vis_utils import plot_model
from data_setting import load_dataset, flatting_images, save_history, convert_to_one_hot
from model_resnet import ResNet50

current_time = time.time()
current_time_str = time.strftime("%Y%m%d_%H%M", time.localtime(current_time))


# Load dataset (hdf5 format)
print("Loading Data... ")
start = time.time()
hdf5_filename = "dataset_1"
x_data, y_data_orig = load_dataset(hdf5_filename)
y_data = convert_to_one_hot(y_data_orig)
print(round(time.time() - start, 2), "s")

print("Input the date : ")
model_path = input()
model_path = "models/" + model_path + "/model.h5"

# Load model
print("Loading model...")
start = time.time()
valid = True

model = load_model(model_path)
model.compile(
    loss=losses.categorical_crossentropy,
    optimizer=optimizers.Adam(lr=1e-6),
    metrics=["accuracy"],
)
print(round(time.time() - start, 2), "s")

history = model.fit(
    x_data,
    y_data,
    validation_split=0.25 * valid,
    epochs=100,
    batch_size=50,
    shuffle=True,
)


print("Saving model...")
start = time.time()
os.mkdir("models/" + current_time_str)
# Save model with json format
model_json = model.to_json()
with open("models/" + current_time_str + "/model" + ".json", "w") as json_file:
    json_file.write(model_json)

# Save weight with h5 format
model.save_weights("models/" + current_time_str + "/weight.h5")

# Save History
save_history(history, current_time_str, valid=valid)
# Plot model with png format
plot_model(
    model,
    to_file="models/" + current_time_str + "/model.png",
    show_shapes=True,
    show_layer_names=True,
)

print(round(time.time() - start, 2), "s")
