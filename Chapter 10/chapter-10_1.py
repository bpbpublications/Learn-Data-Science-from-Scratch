# Decision Tree on the Titanic Dataset

# Importing essential libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Loading the dataset (assuming you've downloaded it from Kaggle and it's in the same directory)
titanic_data = pd.read_csv("titanic.csv")

# Some preprocessing might be needed, like handling missing values and converting categorical features.
# Here's a simplified version:
titanic_data.dropna(inplace=True)
titanic_data.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)
titanic_data = pd.get_dummies(titanic_data, columns=["Sex", "Embarked"], drop_first=True)

# Splitting the dataset into features and target
X = titanic_data.drop("Survived", axis=1)
y = titanic_data["Survived"]

# Splitting data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training our baseline decision tree classifier
clf_baseline = DecisionTreeClassifier(random_state=42)
clf_baseline.fit(X_train, y_train)

# Making predictions
y_pred_baseline = clf_baseline.predict(X_test)

# Measuring accuracy
print("Baseline Model Accuracy:", accuracy_score(y_test, y_pred_baseline))

# Setting the parameters for hyperparameter tuning
from sklearn.model_selection import GridSearchCV
parameters = {'max_depth':range(2,15), 'min_samples_split':range(2,10), 'min_samples_leaf':range(1,10)}

# Using Grid Search for hyperparameter tuning
clf = GridSearchCV(DecisionTreeClassifier(random_state=42), parameters, n_jobs=4)
clf.fit(X=X_train, y=y_train)
best_tree = clf.best_estimator_
print('Hyperparameters of the best model:', clf.best_params_)

# Predicting using the best model
y_pred_tuned = best_tree.predict(X_test)

# Measuring accuracy of the tuned model
print("Tuned Model Accuracy:", accuracy_score(y_test, y_pred_tuned))