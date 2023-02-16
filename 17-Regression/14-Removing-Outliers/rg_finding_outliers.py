"""

Load the file grapes.csv into a Pandas dataframe.

Look at the table of correlations between the variables. Which variable is most highly correlated with weight?

Draw a scatter plot of this variable vs weight.

Are any of the values anomalous? In other words, do any of the values seem out of place compared to the others?

Create a linear regression model to predict weight using the selected variable. Use 70% of the data to train this model. 

When testing the model with the other 30% of the data, what r-squared value is obtained?

"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

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



