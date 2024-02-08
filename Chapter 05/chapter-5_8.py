# Plot customization
import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, color='magenta', label="Dataset 1")
plt.plot(x, y2, color='cyan', label="Dataset 2")

sns.set_palette("husl")
sns.scatterplot(x=x, y=y1, label="Dataset 1")
sns.scatterplot(x=x, y=y2, label="Dataset 2")

plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Customized Plot")

plt.legend()

plt.plot(x, y1, color='magenta', linestyle='dashed', marker='o', label="Dataset 1")
plt.plot(x, y2, color='cyan', linestyle='dotted', marker='s', label="Dataset 2")

plt.show()