from surprise import KNNBasic, Dataset, Reader, accuracy
from surprise.model_selection import cross_validate, train_test_split
# Load the movielens-100k dataset
data = Dataset.load_builtin('ml-100k')
# Sample random trainset and testset
# Test set is made of 25% of the ratings.
trainset, testset = train_test_split(data, test_size=.25)
# Use user_based true/false to switch between user-based or item-based collaborative filtering
algo = KNNBasic(sim_options={'user_based': False})
# Train and test reporting the RMSE and MAE scores
algo.fit(trainset)
predictions = algo.test(testset)
# Then compute RMSE
accuracy.rmse(predictions)