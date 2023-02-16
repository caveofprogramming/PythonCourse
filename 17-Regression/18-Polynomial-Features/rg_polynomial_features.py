from xml.etree.ElementInclude import include
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('cooling.csv')

print(df)

X = df['minute'].values.reshape(-1, 1)
y = df['temperature']

poly = PolynomialFeatures(degree=3, include_bias=False)
poly_features = poly.fit_transform(X)

print(poly_features)