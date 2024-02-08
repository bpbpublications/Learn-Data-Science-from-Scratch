# Import necessary libraries
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# t-SNE
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)

# UMAP
reducer = umap.UMAP()
X_umap = reducer.fit_transform(X)

# Visualization
fig, axs = plt.subplots(1, 3, figsize=(20, 5))

# PCA plot
axs[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y)
axs[0].set_title('PCA')

# t-SNE plot
axs[1].scatter(X_tsne[:, 0], X_tsne[:, 1], c=y)
axs[1].set_title('t-SNE')

# UMAP plot
axs[2].scatter(X_umap[:, 0], X_umap[:, 1], c=y)
axs[2].set_title('UMAP')

plt.show()
