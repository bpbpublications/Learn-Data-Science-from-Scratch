# Range, Variance and Standard Deviation

import numpy as np

data = [10, 15, 20, 25, 30, 35, 40]
range_data = np.max(data) - np.min(data)
print("Range:", range_data)

variance = np.var(data)
print("Variance:", variance)

std_dev = np.std(data)
print("Standard Deviation:", std_dev)