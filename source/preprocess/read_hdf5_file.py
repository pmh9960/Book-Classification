import numpy as np
import h5py
import scipy
import matplotlib.pyplot as plt

f = h5py.File("datasets/dataset_1.hdf5", "r")
images = f[u"train/image"]
labels = f[u"train/label"]

index = 200
image = images[index]
label = labels[index]
plt.imshow(image)
plt.show()
print(label)
