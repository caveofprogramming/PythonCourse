import pandas as pd

df = pd.read_csv('mall_customers.csv')
df.columns = ['id', 'gender', 'age', 'income', 'spending']

df['high spending'] = 0
df.loc[df['spending'] > 90, 'high spending'] = 1

print(df.loc[df['high spending'] == 1].count())