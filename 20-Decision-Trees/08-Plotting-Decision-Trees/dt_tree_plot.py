"""
Import  sklearn.tree.DecisionTreeClassifier
Import the iris dataset
Divide into random test and train segments
Fit the model
Use the fitted model to make predictions about the test segment targets
Use the technique of your choice to assess the accuracy of the predictions.
"""

import re
from collections import defaultdict
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import seaborn as sn
import numpy as np

iris = load_iris(as_frame=True)
target = np.choose(iris['target'], iris['target_names'])
df = iris['data']

X_train, X_test, y_train, y_test = train_test_split(df, target, shuffle=True, train_size=0.7)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)

plot_tree(model, feature_names=df.columns, filled=True, class_names=iris['target_names'])
plt.show()

print(accuracy_score(y_test, y_predicted))

fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(16,9))

axes[0].set_title("True")
axes[1].set_title("Predicted")

print(X_test)
sn.scatterplot(data=X_test, x='petal length (cm)', y='petal width (cm)', hue=y_test, palette='husl', ax=axes[0])
sn.scatterplot(data=X_test, x='petal length (cm)', y='petal width (cm)', hue=y_predicted, palette='husl', ax=axes[1])

plt.show()



