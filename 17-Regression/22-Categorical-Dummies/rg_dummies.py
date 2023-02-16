import pandas as pd

df = pd.read_csv('grapes.csv')
df.drop(67, inplace=True)

df['type'] = pd.get_dummies(df['color'], drop_first=True)
print(df)

