import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {‘ages’: [25, 30, 35, 40, 45, 50, 55, 60],
        ‘incomes’: [30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000]}
df = pd.DataFrame(data)

sns.scatterplot(x=’ages’, y=’incomes’, data=df)
plt.show()