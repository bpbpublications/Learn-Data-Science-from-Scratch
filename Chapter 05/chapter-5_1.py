import pandas as pd

data = {'ages': [25, 30, 35, 40, 45, 50, 55, 60]}
df = pd.DataFrame(data)

print(df['ages'].describe())