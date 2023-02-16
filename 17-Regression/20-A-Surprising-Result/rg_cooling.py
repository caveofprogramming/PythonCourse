from xml.etree.ElementInclude import include
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

df = pd.read_csv('cooling.csv')

print(df)

X = df['minute'].values.reshape(-1, 1)
y = df['temperature']

model = LinearRegression()
model.fit(X, y**-2)

y_pred = model.predict(X)

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot()

ax.scatter(X, y)
ax.plot(X, y_pred**(-1/2))

print(r2_score(y, y_pred**(-1/2)))

plt.show()
