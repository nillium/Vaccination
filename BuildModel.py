from pathlib import Path
import numpy as np
import keras
from keras.layers import Dense, InputLayer, Flatten, Conv2D, MaxPooling2D


def build_model():

    dataset = np.load('data/dataset.npy')
    labels = np.load('data/labels.npy')
    print('data loaded')
    print('Dataset Shape: ' + str(dataset.shape))
    print('Labels Shape: ' + str(labels.shape))

    x_train = dataset[0:79]
    x_train = x_train / 255

    x_test = dataset[80:99]
    x_test = x_test / 255

    y_train = labels[0:79]
    y_test = labels[80:99]

    print("x-train Shape: " + str(x_train.shape))
    print("x-test Shape: " + str(x_test.shape))
    print("y-train Shape: " + str(y_train.shape))
    print("y-test Shape: " + str(y_test.shape))

    def initialize_kernel(shape, dtype=None):
        filters = np.load('data/custom_filter.npy')
        return filters

    # Build the model
    model = keras.Sequential()
    model.add(InputLayer(input_shape=(64, 256, 1)))
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
    model.fit(x_train, y_train, epochs=20, batch_size=32)

    # Evaluate the model
    score = model.evaluate(x_test, y_test)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    return model
