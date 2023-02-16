import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

"""
1. Acquire data
2. Explore
3. Clean data
4. Train/test split
5. Normalise
6. Fit model
7. Metrics
"""

df = pd.read_csv('mall_customers.csv')
df.columns = ['id', 'gender', 'age', 'income', 'spending']

df['high spending'] = 0
df.loc[df['spending'] > 90, 'high spending'] = 1

print(df.loc[df['high spending'] == 1].count())

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot(projection='3d')
ax.scatter(df['age'], df['income'], df['spending'])
plt.show()

X = df[['age', 'income']]
y = df['high spending']

(X_train, X_test, y_train, y_test) = train_test_split(X, y, train_size=0.7, shuffle=True)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(X_train, y_train)

print(f'{model.score(X_test, y_test)}')