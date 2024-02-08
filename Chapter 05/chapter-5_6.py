# Line Plot
import seaborn as sns
import matplotlib.pyplot as plt

days = list(range(1, 31))
temperatures = [23, 24, 26, 24, 22, 20, 25, 23, 24, 26, 28, 27, 24, 22, 23, 25, 27, 26, 24, 23, 25, 26, 27, 29, 28, 26, 25, 24, 26, 27]

sns.lineplot(x=days, y=temperatures)
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.show()