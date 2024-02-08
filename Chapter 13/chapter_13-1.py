1.	from sklearn.cluster import KMeans
2.	from sklearn.datasets import load_iris
3.	import matplotlib.pyplot as plt
4.	
5.	iris = load_iris()
6.	X = iris.data

1.	wcss = [] 
2.	for i in range(1, 11):
3.	    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
4.	    kmeans.fit(X)
5.	    wcss.append(kmeans.inertia_)
6.	
7.	plt.plot(range(1, 11), wcss)
8.	plt.title('The Elbow Method')
9.	plt.xlabel('Number of clusters')
10.	plt.ylabel('WCSS') 
11.	plt.show()

1.	kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
2.	pred_y = kmeans.fit_predict(X)

1.	plt.scatter(X[pred_y == 0, 0], X[pred_y == 0, 1], s=100, c='red', label ='Cluster 1')
2.	plt.scatter(X[pred_y == 1, 0], X[pred_y == 1, 1], s=100, c='blue', label ='Cluster 2')
3.	plt.scatter(X[pred_y == 2, 0], X[pred_y == 2, 1], s=100, c='green', label ='Cluster 3')
4.	plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label = 'Centroids')
5.	plt.title('Clusters of Iris')
6.	plt.legend()
7.	plt.show()