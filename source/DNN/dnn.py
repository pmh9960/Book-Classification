from keras.models import Sequential
from keras.layers.core import Dense
from keras import optimizers, initializers, losses
import numpy as np
import tensorflow as tf
import keras
import matplotlib.pyplot as plt
import time, os
from keras.utils.vis_utils import plot_model
from data_setting import load_dataset, flatting_images, save_history

current_time = time.time()
current_time_str = time.strftime("%Y%m%d_%H%M", time.localtime(current_time))

# Load dataset (hdf5 format)
print("Loading Data... ")
start = time.time()
hdf5_filename = "dataset_1"
x_data_orig, y_data_orig = load_dataset(hdf5_filename)
# Flatting
x_data, m_data, input_dim = flatting_images(x_data_orig)
# plt.imshow(x_data[5].reshape((140, 108, 3)))
# plt.show()
# print(x_data)
# print(m_data, input_dim)

# One hot encoding
num = np.unique(y_data_orig, axis=0)
output_dim = num.shape[0]
y_data = np.eye(output_dim)[y_data_orig]
print(round(time.time() - start, 2), "s")


# Make model
print("Making model...")
start = time.time()
model = Sequential()
# print(f"(input_dim, output_dim) = ({input_dim}, {output_dim})")
layers_dim = [input_dim, 1000, output_dim]
valid = False

# First hidden layer
model.add(
    Dense(
        layers_dim[1],
        input_dim=layers_dim[0],
        activation="relu",
        kernel_initializer=initializers.he_normal(),
    )
)
# Hidden layers
for i in range(len(layers_dim) - 3):
    model.add(
        Dense(
            layers_dim[i + 2],
            activation="relu",
            kernel_initializer=initializers.he_normal(),
        )
    )
# Output layer
model.add(
    Dense(
        layers_dim[len(layers_dim) - 1],
        activation="softmax",
        kernel_initializer=initializers.he_normal(),
    )
)

model.compile(
    loss=losses.categorical_crossentropy,
    optimizer=optimizers.Adam(lr=1e-6),
    metrics=["accuracy"],
)
print(round(time.time() - start, 2), "s")
print(layers_dim)

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

save_history(history, current_time_str, valid=valid)


plot_model(model, to_file="models/" + current_time_str + "/model.png", show_shapes=True)
print(round(time.time() - start, 2), "s")
