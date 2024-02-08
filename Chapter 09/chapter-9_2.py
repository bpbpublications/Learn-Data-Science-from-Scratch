# Naive Bayes Classifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load the breast cancer dataset
data = load_breast_cancer()

# Split the data into input features (X) and target variable (y)
X, y = data.data, data.target

# Split the data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian Naive Bayes object
gnb = GaussianNB()

# Train the model using the training sets
gnb.fit(X_train, y_train)

# Predict the response for the test dataset
y_pred = gnb.predict(X_test)

# Print the accuracy score of the model
print("Accuracy: ", accuracy_score(y_test, y_pred))