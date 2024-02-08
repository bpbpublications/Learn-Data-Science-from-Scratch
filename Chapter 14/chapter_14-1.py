# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape data to fit the model
x_train = x_train.reshape(60000, 28, 28, 1)
x_test = x_test.reshape(10000, 28, 28, 1)

# One-hot encoding for target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Initialize the model
model = Sequential()  # This initializes a linear stack of layers

# Add a convolutional layer with 64 filters, a 3x3 window, and ReLU activation function.
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28, 28, 1)))

# Add another convolutional layer
model.add(Conv2D(32, kernel_size=3, activation='relu'))

# Add a max pooling layer
model.add(MaxPooling2D(pool_size=(2, 2)))

# Flatten the 2D arrays for fully connected layers
model.add(Flatten())

# Add a dense layer with 10 neurons (for the 10 digits we have in the dataset) and softmax activation.
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5)
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy*100:.2f}%")