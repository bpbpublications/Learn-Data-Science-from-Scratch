1.	# Importing necessary libraries
2.	from sklearn import datasets
3.	from sklearn.model_selection import train_test_split
4.	from sklearn.preprocessing import StandardScaler
5.	from sklearn import svm
6.	from sklearn.metrics import mean_squared_error
7.	
8.	# Load the California housing dataset
9.	california = datasets.fetch_california_housing()
10.	X = california.data
11.	y = california.target
12.	
13.	# Split the dataset into a training set and a test set
14.	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
15.	
16.	# Standardize the features
17.	scaler = StandardScaler()
18.	X_train_std = scaler.fit_transform(X_train)
19.	X_test_std = scaler.transform(X_test)
20.	
21.	# Create a SVM regressor
22.	regr = svm.SVR(kernel='linear')
23.	
24.	# Train the regressor
25.	regr.fit(X_train_std, y_train)
26.	
27.	# Make predictions
28.	y_pred = regr.predict(X_test_std)
29.	
30.	# Evaluate the model
31.	print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
