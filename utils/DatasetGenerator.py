import numpy as np
import random
import cv2
from pathlib import Path
import os, sys

sys.path.append('../Vaccination')
from Configuration import *

# Number of samples to be generated


# Label and dataset initiation
dataset = np.zeros((number_of_total_samples, sample_h, sample_w))
labels = np.zeros(number_of_total_samples)

# where signal starts and ends, does not mean anything if noise
x1 = round(sample_w / 4)
x2 = round(3 * sample_w / 4)

for i in range(0, number_of_total_samples - 1):
    noise_or_sin = random.choice([1, 2])
    if noise_or_sin == 1:
        noise = np.zeros((sample_h, sample_w))
        pen = round(sample_h / 2)
        for j in range(0, sample_w - 1):
            if pen < (sample_h - 1) or pen > 0:
                noise[pen, j] = 255
            if pen == (sample_h - 1):
                pen = pen - 1
            if pen == 0:
                pen = pen + 1
            direction = random.choice([-1, 1])
            pen = pen + direction

        dataset[i, :, :] = noise
        labels[i] = 0

    if noise_or_sin == 2:
        sign = np.zeros((sample_h, sample_w))
        pen = round(sample_h / 2)
        for j in range(0, x1):
            if 0 < pen < sample_h:
                sign[pen, j] = 255
            if pen >= sample_h:
                pen = pen - 1
            if pen <= 0:
                pen = pen + 1
            direction = random.choice([-1, 1])
            pen = pen + direction
        for j in range(x1, x2):
            pen = pen + (1 * np.sin(8 * np.pi * ((j - x1) / x2 - 1 - x1)))
            pen = round(pen)

            if 0 < pen < sample_h:
                sign[pen, j] = 255
            if pen >= sample_h:
                pen = sample_h - 1
            if pen <= 0:
                pen = 0
        for j in range(x2, sample_w):
            pen = round(pen)
            if 0 < pen < sample_h:
                sign[pen, j] = 255
            if pen >= sample_h:
                pen = pen - 1
            if pen <= 0:
                pen = pen + 1
            direction = random.choice([-1, 1])
            pen = pen + direction

        dataset[i, :, :] = sign
        labels[i] = 1

    cv2.imshow('dataset', dataset[i])
    root_dir = Path(__file__).resolve().parent.parent
    train_sample_path = Path("data/train/" + 'train_sample_%s.png' % str(i))
    test_sample_path = Path("data/test/" + 'test_sample_%s.png' % str(i))
    if i < number_of_training_samples:
        cv2.imwrite(str(Path.joinpath(root_dir, train_sample_path)), dataset[i])
        cv2.waitKey(10)
    if i >= number_of_training_samples:
        cv2.imwrite(str(Path.joinpath(root_dir, test_sample_path)), dataset[i])
        cv2.waitKey(10)

# Save labels and dataset as numpy array files
dataset_path = Path("data/dataset.npy")
labels_path = Path("data/labels.npy")
root_dir = Path(__file__).resolve().parent.parent
np.save(Path.joinpath(root_dir, dataset_path), dataset)
np.save(Path.joinpath(root_dir, labels_path), labels)

