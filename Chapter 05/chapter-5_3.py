# Mean, Median and Mode
import numpy as np

data = [10, 15, 20, 25, 30, 35, 40]
mean = np.mean(data)
print("Mean:", mean)

median = np.median(data)
print("Median:", median)

from scipy import stats
	
data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 7]
mode = stats.mode(data)
print("Mode:", mode.mode[0])