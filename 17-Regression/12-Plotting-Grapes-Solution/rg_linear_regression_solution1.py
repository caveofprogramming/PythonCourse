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

df = pd.read_csv("grapes.csv")
print(df.corr())

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot()
ax.set_xlabel("Diameter")
ax.set_ylabel("Weight")
ax.scatter(df['diameter'], df['weight'])
plt.show()