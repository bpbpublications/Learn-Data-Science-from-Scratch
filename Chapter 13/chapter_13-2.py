1.	# Import necessary libraries
2.	from sklearn.datasets import load_iris
3.	from sklearn.preprocessing import StandardScaler
4.	from scipy.cluster.hierarchy import dendrogram, linkage
5.	from matplotlib import pyplot as plt
6.	
7.	# Load the iris dataset
8.	iris = load_iris()
9.	X = iris.data
10.	
11.	# Standardize the features for better results
12.	scaler = StandardScaler()
13.	X_scaled = scaler.fit_transform(X)
14.	
15.	# Perform hierarchical clustering
16.	linked = linkage(X_scaled, 'ward')
17.	
18.	# Plot the dendrogram
19.	plt.figure(figsize=(10, 7))
20.	dendrogram(linked,
21.	            orientation='top',
22.	            distance_sort='descending',
23.	            show_leaf_counts=True)
24.	plt.show()
