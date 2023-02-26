from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
import matplotlib.pyplot as plt


housing = fetch_california_housing(as_frame=True)

X = housing['data']
y = housing['target']

X = MinMaxScaler().fit_transform(X)

X = X[:20, :2]
y = y[:20]

X_train, X_test_validate, y_train, y_test_validate = train_test_split(X, y, shuffle=True, train_size=0.7)

X_validate, X_test, y_validate, y_test = train_test_split(X_test_validate, y_test_validate, shuffle=True, train_size=0.5)

model = Sequential()
model.add(Dense(2000, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(2000, activation='relu'))
model.add(Dense(2000, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_absolute_percentage_error')

history = model.fit(X_train, y_train, batch_size=32, epochs=300, validation_data=(X_validate, y_validate))

loss = model.evaluate(X_test, y_test)

print(f'Loss (mean percentage error): {loss:.2f}')

y_predicted = model.predict(X_test)

fig, ax = plt.subplots()

ax.plot(history.history['loss'], color='red', label='Training Loss')
ax.plot(history.history['val_loss'], color='blue', label='Validation Loss')
ax.legend()
plt.show()