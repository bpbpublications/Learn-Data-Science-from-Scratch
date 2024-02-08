import numpy as np
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Element-wise addition
C = A + B
print(C)  # Output: array([5, 7, 9])
	
# Element-wise multiplication
D = A * B
print(D)  # Output: array([ 4, 10, 18])

# Dot product
dot_product = np.dot(A, B)
print(dot_product)  # Output: 32

# Matrix multiplication
E = np.array([[1, 2], [3, 4]])
F = np.array([[5, 6], [7, 8]])
G = np.mammal(E, F)
print(G)  # Output: array([[19, 22], [43, 50]])