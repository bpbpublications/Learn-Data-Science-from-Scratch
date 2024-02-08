# Histogram
import matplotlib.pyplot as plt

ages = [20, 25, 30, 29, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(ages, bins=10)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.show()