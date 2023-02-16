import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('grapes.csv')
df.drop(67, inplace=True)

df['type'] = pd.get_dummies(df['color'], drop_first=True)
df.sort_values(by='weight', inplace=True)

x = df['weight']
y = df['type']
X = df[['weight', 'diameter', 'length']]

(X_train, X_test, y_train, y_test) = train_test_split(X, y, train_size=0.7, shuffle=True)


model = LogisticRegression(solver="liblinear", random_state=0)
model.fit(X_train, y_train)

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot()

ax.set_xlabel("Weight")
ax.set_ylabel("Type")

ax.scatter(x,y)

plt.show()

print(f'{model.score(X_test, y_test):.2f}')

