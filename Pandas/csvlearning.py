import pandas as pd

# data = pd.read_csv('./complete-pandas-tutorial/warmup-data/coffee.csv')
# data = pd.read_parquet('./complete-pandas-tutorial/data/results.parquet')
data = pd.read_excel('./complete-pandas-tutorial/data/olympics-data.xlsx')
df = pd.DataFrame(data)
# df = pd.DataFrame(data)
# print(df.columns)
# print(df['year'].tolist())
print(df)
