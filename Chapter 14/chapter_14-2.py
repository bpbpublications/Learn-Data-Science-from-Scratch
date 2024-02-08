from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

# Load dataset
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000) # Limiting to top 10,000 frequent words

# Pad each sequence to the same length (let's use a max length of 500)
maxlen = 500
train_data = sequence.pad_sequences(train_data, maxlen=maxlen)
test_data = sequence.pad_sequences(test_data, maxlen=maxlen)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Initialize the model
model = Sequential()

# Add an embedding layer
model.add(Embedding(10000, 32, input_length=maxlen))

# Add an RNN layer
model.add(SimpleRNN(32))

# Add a dense layer for classification
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_data, train_labels, epochs=10, batch_size=128, validation_split=0.2)

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(test_data, test_labels)
print("Test Accuracy:", test_acc)