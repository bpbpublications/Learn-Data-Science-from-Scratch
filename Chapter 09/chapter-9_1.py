# KNN
import numpy as np
import pandas as pd

np.random.seed(0)
n = 100
hours_studied = np.random.normal(30.0, 10.0, n)
hours_slept = np.random.normal(8.0, 3.0, n)

# We make the test score a function of study hours and sleep, plus some noise
test_score = hours_studied + hours_slept + np.random.normal(0, 10.0, n)

student_scores_df = pd.DataFrame({'hours_studied': hours_studied, 'hours_slept': hours_slept, 'test_score': test_score})

from sklearn.model_selection import train_test_split
X = student_scores_df[['hours_studied', 'hours_slept']]
y = student_scores_df['test_score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.neighbors import KNeighborsRegressor
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)