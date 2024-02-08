# Stacking
import numpy as np

A = np.array([1, 2, 3, 4, 5, 6])
B = A.reshape((2, 3))

print(B)
# Output:
# array([[1, 2, 3],
#        [4, 5, 6]])