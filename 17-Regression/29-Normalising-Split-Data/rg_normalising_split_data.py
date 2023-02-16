import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('grapes.csv')

X = df[['length', 'diameter']]
y = df['weight']

scaler = StandardScaler()

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)