import pandas as pd

data = pd.read_csv('./coffee.csv')
# print(data)
df = pd.DataFrame(data)
print(df.head(3))