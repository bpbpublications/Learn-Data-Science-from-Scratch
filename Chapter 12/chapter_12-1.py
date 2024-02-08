import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Loading the Iris dataset
data = load_iris()
X = data.data
y = data.target
labels = data.target_names

# Standardizing the dataset
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Applying PCA and reducing to 2 components
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(X_std)

# Plotting the 2D data
plt.figure(figsize =(8, 6))

# Using different colors for different classes in the Iris dataset
colors = ['r', 'g', 'b']
for i, color in zip(range(len(labels)), colors):
    plt.scatter(principalComponents[y == i, 0], 
                principalComponents[y == i, 1], 
                color=color, 
                label=labels[i])

plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.legend(loc="best")
plt.title("PCA of Iris Dataset")
plt.show()