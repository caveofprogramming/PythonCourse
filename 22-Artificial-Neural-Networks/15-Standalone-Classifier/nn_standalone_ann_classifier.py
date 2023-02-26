from keras.datasets import mnist
from sklearn.metrics import accuracy_score
import numpy as np
import joblib

(X_train, y_train), (X_test, y_test) = mnist.load_data()

ann = joblib.load('mnist.ann')

y_predicted = ann.predict(X_test.reshape(len(X_test), -1))

y_predicted = np.argmax(y_predicted, axis=1)

print("Score:", accuracy_score(y_test, y_predicted))