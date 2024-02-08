# Create a simple plot
import matplotlib.pyplot as plt

# Create a simple line plot
plt.plot(x, y)

# Customize the plot with colors, markers, labels, and more
plt.plot(x, y, color='red', marker='o', linestyle='--', label='My Data')
plt.legend()

# Save your masterpiece as a high-quality image file
plt.savefig('my_plot.png', dpi=300)