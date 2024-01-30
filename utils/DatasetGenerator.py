import numpy as np
import random
import cv2
from pathlib import Path

# Number of samples to be generated
number_of_data = 120

# Sample dimensions
data_w = 256
data_h = 64

# Label and dataset initiation
dataset = np.zeros((number_of_data, data_h, data_w))
labels = np.zeros(number_of_data)

# where signal starts and ends, does not mean anything if noise
x1 = round(data_w / 4)
x2 = round(3 * data_w / 4)

for i in range(0, number_of_data - 1):
    noise_or_sin = random.choice([1, 2])
    if noise_or_sin == 1:
        noise = np.zeros((data_h, data_w))
        pen = round(data_h / 2)
        for j in range(0, data_w - 1):
            if pen < (data_h - 1) or pen > 0:
                noise[pen, j] = 255
            if pen == (data_h - 1):
                pen = pen - 1
            if pen == 0:
                pen = pen + 1
            direction = random.choice([-1, 1])
            pen = pen + direction

        dataset[i, :, :] = noise
        labels[i] = 0

    if noise_or_sin == 2:
        sign = np.zeros((data_h, data_w))
        pen = round(data_h / 2)
        for j in range(0, x1):
            if 0 < pen < data_h:
                sign[pen, j] = 255
            if pen >= data_h:
                pen = pen - 1
            if pen <= 0:
                pen = pen + 1
            direction = random.choice([-1, 1])
            pen = pen + direction
        for j in range(x1, x2):
            pen = pen + (1 * np.sin(8 * np.pi * ((j - x1) / x2 - 1 - x1)))
            pen = round(pen)

            if 0 < pen < data_h:
                sign[pen, j] = 255
            if pen >= data_h:
                pen = data_h - 1
            if pen <= 0:
                pen = 0
        for j in range(x2, data_w):
            pen = round(pen)
            if 0 < pen < data_h:
                sign[pen, j] = 255
            if pen >= data_h:
                pen = pen - 1
            if pen <= 0:
                pen = pen + 1
            direction = random.choice([-1, 1])
            pen = pen + direction

        dataset[i, :, :] = sign
        labels[i] = 1

    cv2.imshow('dataset', dataset[i])
    cv2.imwrite('sample_%d.png' % i, dataset[i])
    cv2.waitKey(10)

# Save labels and dataset as numpy array files
dataset_path = Path("data/dataset.npy")
labels_path = Path("data/labels.npy")
root_dir = Path(__file__).resolve().parent.parent
np.save(Path.joinpath(root_dir, dataset_path), dataset)
np.save(Path.joinpath(root_dir, labels_path), labels)

