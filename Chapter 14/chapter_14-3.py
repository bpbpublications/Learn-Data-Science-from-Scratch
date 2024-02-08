import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from tensorflow.keras.preprocessing import sequence

# Load the dataset
max_features = 10000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)

# Pad the sequences to have a uniform length
maxlen = 80  # Only consider the first 80 words of each movie review
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)

model = Sequential()

# Starting off with an efficient embedding layer which maps our vocab indices into embedding_dims dimensions
embedding_dims = 128
model.add(Embedding(max_features, embedding_dims, input_length=maxlen))

# Adding LSTM layer with 128 memory units
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))  # Because this is a binary classification problem

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print(model.summary())

model.fit(X_train, y_train, batch_size=32, epochs=3, validation_data=(X_test, y_test))

print("Training complete!")
