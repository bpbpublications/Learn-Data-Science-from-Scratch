1.	from sklearn import svm
2.	
3.	# Assign class_weight='balanced' to handle imbalanced classes
4.	clf = svm.SVC(kernel='linear', class_weight='balanced')
5.	
6.	# Fit the model on your training data
7.	clf.fit(X_train_std, y_train)
8.	
9.	# Make predictions on your test data
10.	y_pred = clf.predict(X_test_std)