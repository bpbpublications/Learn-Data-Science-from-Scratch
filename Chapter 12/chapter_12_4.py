1.	from sklearn import svm, datasets
2.	from sklearn.model_selection import GridSearchCV
3.	
4.	# Load iris dataset as an example
5.	iris = datasets.load_iris()
6.	parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
7.	
8.	svc = svm.SVC()
9.	
10.	clf = GridSearchCV(svc, parameters)
11.	
12.	clf.fit(iris.data, iris.target)
13.	
14.	# Let's print the best parameters found by GridSearchCV
15.	print("Best parameters found: ", clf.best_params_)