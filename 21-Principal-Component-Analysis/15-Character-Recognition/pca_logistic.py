from keras.datasets import mnist
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(len(X_train), -1)
X_test = X_test.reshape(len(X_test), -1)

print("PCA ...")
pca = PCA(0.95)
X_train_pc = pca.fit_transform(X_train)
X_test_pc = pca.transform(X_test)

print("Number of components:", pca.n_components_)

print("Logistic regression...")
model = LogisticRegression()
model.fit(X_train_pc, y_train)

y_predicted = model.predict(X_test_pc)

print("Score:", accuracy_score(y_test, y_predicted))
