"""
Build a neural network to recognise digits in the MNIST dataset.
Display a chart showing only digits that were NOT recognised correctly.
"""

from keras.datasets import mnist
from keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(len(X_train), -1)
X_test = X_test.reshape(len(X_test), -1)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


