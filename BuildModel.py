import numpy as np
import keras
from keras.layers import Dense, InputLayer, Flatten, Conv2D, MaxPooling2D
from Configuration import *


def build_model():

    dataset = np.load('data/dataset.npy')
    labels = np.load('data/labels.npy')
    print('data loaded')
    print('Dataset Shape: ' + str(dataset.shape))
    print('Labels Shape: ' + str(labels.shape))

    x_train = dataset[0:number_of_training_samples]
    x_train = x_train / 255

    x_test = dataset[(number_of_training_samples+1):(number_of_total_samples-1)]
    x_test = x_test / 255

    y_train = labels[0:number_of_training_samples]
    y_test = labels[(number_of_training_samples+1):(number_of_total_samples-1)]

    print("x-train Shape: " + str(x_train.shape))
    print("x-test Shape: " + str(x_test.shape))
    print("y-train Shape: " + str(y_train.shape))
    print("y-test Shape: " + str(y_test.shape))

    def initialize_kernel(shape, dtype=None):
        filters = np.load('data/custom_filter.npy')
        return filters

    # Build the model
    model = keras.Sequential()
    model.add(InputLayer(input_shape=(sample_h, sample_w, 1)))
    model.add(Conv2D(4, kernel_size=(16, 16), kernel_initializer=initialize_kernel))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, kernel_size=(2, 2), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    model.summary()
    # Train the model
    model.fit(x_train, y_train, epochs=epochs, batch_size=32)

    # Evaluate the model
    score = model.evaluate(x_test, y_test)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    return model
