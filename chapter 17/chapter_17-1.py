import pickle
# Here's a simple Python object - a dictionary
data = {"name": "John", "age": 30, "city": "New York"}
# Now, let's serialize (pickle) it
serialized_data = pickle.dumps(data)
# Now, let's deserialize (unpickle) it
deserialized_data = pickle.loads(serialized_data)
# And we're back to the original data
print(deserialized_data)