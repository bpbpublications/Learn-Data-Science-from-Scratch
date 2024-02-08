import numpy as np

# Creating a 1D array
one_dim_array = np.array([1, 2, 3, 4, 5])
print(one_dim_array)  # Output: array([1, 2, 3, 4, 5])

# Creating a 2D array
two_dim_array = np.array([[1, 2], [3, 4], [5, 6]])
print(two_dim_array)  # Output: array([[1, 2], [3, 4], [5, 6]])

# Indexing
print(one_dim_array[2])  # Output: 3

# Slicing
print(one_dim_array[1:4])  # Output: array([2, 3, 4])

# Accessing elements in a 2D array
print(two_dim_array[1, 0])  # Output: 3

# Reshaping
reshaped_array = one_dim_array.reshape(5, 1)
print(reshaped_array)  # Output: array([[1], [2], [3], [4], [5]])

# Transposing
transposed_array = two_dim_array.T
print(transposed_array)  # Output: array([[1, 3, 5], [2, 4, 6]])