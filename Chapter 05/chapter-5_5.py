# Bar plot
import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Toys']
items_sold = [120, 200, 150]

plt.bar(categories, items_sold)
plt.xlabel('Categories')
plt.ylabel('Items Sold')
plt.show()