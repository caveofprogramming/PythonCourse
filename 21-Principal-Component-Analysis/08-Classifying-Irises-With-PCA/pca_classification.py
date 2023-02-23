from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris(as_frame=True)
X = iris['data']
y = np.choose(iris['target'], iris['target_names'])

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.7)

pca = PCA(2)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

y_predicted = tree.predict(X_test)

df = pd.DataFrame(pca.components_)
df.columns = X.columns
print(df)

print('Accuracy:', accuracy_score(y_test, y_predicted))

fig, axes = plt.subplots(ncols=2)

ax = axes[0]
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_title("True")
sn.scatterplot(x=X_test[:,0], y=X_test[:,1], hue=y_test, palette='husl', ax=ax)

ax = axes[1]
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_title("True")
sn.scatterplot(x=X_test[:,0], y=X_test[:,1], hue=y_predicted, palette='husl', ax=ax)

plt.show()
