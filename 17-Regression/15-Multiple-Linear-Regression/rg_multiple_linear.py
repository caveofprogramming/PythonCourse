import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

"""
a + bx = y
a + bx1 + cx2 + dx3 .... = y
"""

df = pd.read_csv("grapes.csv")
df.drop(67, inplace=True)
print(df.corr())

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot()
ax.set_xlabel("Diameter")
ax.set_ylabel("Weight")
ax.scatter(df['diameter'], df['weight'])

X = df["diameter"].values.reshape(-1, 1)
y = df["weight"]

(X_train, X_test, y_train, y_test) = train_test_split(X, y, train_size=0.7, shuffle=False)

model = LinearRegression()
model.fit(X_train, y_train)

y_line = model.predict(X)
ax.plot(X, y_line)
plt.show()

y_predicted = model.predict(X_test)
r2 = r2_score(y_test, y_predicted)

print(r2)

df['error'] = abs(y_line - y)

print(df.sort_values(by='error'))



