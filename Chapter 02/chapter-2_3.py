import numpy as np
	
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([1, 0, -1])
	
# Broadcasting B to match the shape of A
C = A + B
print(C)
# Output:
# array([[ 2,  2,  2],
#        [ 5,  5,  5],
#        [ 8,  8,  8]])