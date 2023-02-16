import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df1 = pd.read_csv('grapes.csv')

df1.drop(columns='color', inplace=True)

df1['weight'] *= 10

print(df1.agg(['min', 'max', 'var', 'mean']))

scaler = StandardScaler()
X = scaler.fit_transform(df1)
df2 = pd.DataFrame(X, columns=df1.columns)
print(df2.agg(['min', 'max', 'var', 'mean']))

scaler = MinMaxScaler(feature_range=(-1, 1))
X = scaler.fit_transform(df1)
df3 = pd.DataFrame(X, columns=df1.columns)
print(df3.agg(['min', 'max', 'var', 'mean']))

