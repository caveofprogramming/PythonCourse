from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.utils import to_categorical

iris = load_iris(as_frame=True)
X = iris['data']
y = iris['target']

(X_train, X_test, y_train, y_test) = train_test_split(X, y, shuffle=True, train_size=0.7)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print(y_test[:4])


