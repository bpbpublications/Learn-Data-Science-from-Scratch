# Splitting
G = np.array([[1, 2, 3], [4, 5, 6]])

# Vertical splitting
H, I = np.vsplit(G, 2)
print(H)  # Output: array([[1, 2, 3]])
print(I)  # Output: array([[4, 5, 6]])

# Horizontal splitting
J, K, L = np.hsplit(G, 3)
print(J)  # Output: array([[1], [4]])
print(K)  # Output: array([[2], [5]])
print(L)  # Output: array([[3], [6]])