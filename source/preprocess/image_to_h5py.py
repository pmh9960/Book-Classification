import numpy as np
import h5py
import scipy
from PIL import Image
from scipy import ndimage
import os

folder_names = os.listdir("sample_images")
path_hdf5 = "datasets/dataset_1.hdf5"
# images128 = []
# images256 = []
# images512 = []
images = []
labels = []

index = 0
for folder_name in folder_names:
    files = os.listdir("sample_images/" + folder_name)
    for file in files:
        image = np.array(ndimage.imread("sample_images/" + folder_name + "/" + file))
        images.append(image)
        labels.append(index)
    index += 1

f = h5py.File(path_hdf5, "w")
train = f.create_group("train")
# dev = f.create_group("dev")
# test = f.create_group("test")
train.attrs["desc"] = "Training set"
# dev.attrs["desc"] = "Development set"
# test.attrs["desc"] = "Test set"

train.create_dataset("image", dtype="int32", data=images)
train.create_dataset("label", dtype="int32", data=labels)
f.close()
