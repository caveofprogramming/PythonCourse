
"""
Use load_wine to load the wine dataset
Scale the data and use PCA to find the components that explain 95% of the variance
Split the data into test and train segments
Use a decision tree to try to predict the class of wine using the principle components
Score your model using the metric of your choice
Which feature of the original data was the biggest contributor to each of the components?
"""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

wine = load_wine(as_frame=True)
X = wine['data']
y = np.choose(wine['target'], wine['target_names'])

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True)

print("Input data: ", X_train.shape)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

pca = PCA(0.95)

X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

print("Components: ", pca.n_components_)

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

y_predicted = tree.predict(X_test)

print("Score:", accuracy_score(y_test, y_predicted))

for i in range(pca.n_components_):
    print(f'Principle component {i} greatest contributor:', X.columns[np.argmax(X_train[i])])
