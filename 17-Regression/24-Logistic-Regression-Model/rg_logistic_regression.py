import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('grapes.csv')
df.drop(67, inplace=True)

df['type'] = pd.get_dummies(df['color'], drop_first=True)
df.sort_values(by='weight', inplace=True)

x = df['weight']
y = df['type']
X = x.values.reshape(-1, 1)


model = LogisticRegression(solver="liblinear", random_state=0)
model.fit(X, y)

print(model.intercept_, model.coef_)

a = model.intercept_[0]
b = model.coef_[0][0]
y_logistic = 1/(1 + np.exp(-(a + b*x)))

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot()

ax.set_xlabel("Weight")
ax.set_ylabel("Type")

ax.scatter(x,y)
ax.plot(x, y_logistic, color='red')

plt.show()

print(f'{model.score(X, y):.2f}')

