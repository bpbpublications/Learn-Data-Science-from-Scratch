1.	from sklearn.cluster import DBSCAN
2.	from sklearn import datasets
3.	
4.	# Load Iris data
5.	iris = datasets.load_iris()
6.	X = iris.data
7.	
8.	# Apply DBSCAN
9.	dbscan = DBSCAN(eps=0.5, min_samples=5)
10.	clusters = dbscan.fit_predict(X)
11.	
12.	print("DBSCAN cluster labels: ", clusters)
