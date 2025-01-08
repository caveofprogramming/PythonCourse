import pandas as pd

df = pd.read_csv("grapes.csv")
print(df)
#print(df.drop('color', axis=1).corr())
print(df[['weight', 'length', 'diameter']].corr())
#print(df.corr())
