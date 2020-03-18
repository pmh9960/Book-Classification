import numpy as np
import h5py
import matplotlib.pyplot as plt


def load_dataset(hdf5_filename):
    dataset = h5py.File("datasets/" + hdf5_filename + ".hdf5", "r")
    train_set_image = np.array(dataset["train/image"][:])
    train_set_label = np.array(dataset["train/label"][:])

    # dev_set_image = np.array(dataset["dev/image"][:])
    # dev_set_label = np.array(dataset["dev/label"][:])

    # test_set_image = np.array(dataset["test/image"][:])
    # test_set_label = np.array(dataset["test/label"][:])

    # dataset = (
    #     train_set_image,
    #     train_set_label,
    #     dev_set_image,
    #     dev_set_label,
    #     test_set_image,
    #     test_set_label,
    # )
    # return dataset

    return train_set_image, train_set_label


def convert_to_one_hot(y_data_orig):
    num = np.unique(y_data_orig, axis=0)
    num = num.shape[0]
    return np.eye(num)[y_data_orig]


def flatting_images(train_set_X):
    m_train = train_set_X.shape[0]
    train_set_X_flatten = train_set_X.reshape((m_train, -1)) / 255.0
    dim = train_set_X_flatten.shape[1]

    return train_set_X_flatten, m_train, dim


def save_history(history, current_time_str, valid=True):
    # Plot training & validation accuracy values
    plt.plot(history.history["acc"])
    if valid:
        plt.plot(history.history["val_acc"])
    plt.title("Model accuracy")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    if valid:
        plt.legend(["Train", "Test"], loc="upper left")
    else:
        plt.legend(["Train"], loc="upper left")
    plt.savefig("models/" + current_time_str + "/history_accuracy.png")
    plt.clf()  # Clear PLT

    # Plot training & validation loss values
    plt.plot(history.history["loss"])
    if valid:
        plt.plot(history.history["val_loss"])
    plt.title("Model loss")
    plt.ylabel("Loss")
    plt.xlabel("Epoch")
    if valid:
        plt.legend(["Train", "Test"], loc="upper left")
    else:
        plt.legend(["Train"], loc="upper left")
    plt.savefig("models/" + current_time_str + "/history_loss.png")
    plt.clf()

