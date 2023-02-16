import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv('grapes.csv')
df.drop(67, inplace=True)

x = df['weight']
y = df['color']
#X = df[['weight', 'diameter', 'length']]
X = df[['length']]

(X_train, X_test, y_train, y_test) = train_test_split(X, y, train_size=0.7, shuffle=True)

model = LogisticRegression(solver="liblinear", random_state=0)
model.fit(X_train, y_train)

plt.show()

print(f'{model.score(X_test, y_test):.2f}')
 
cm = confusion_matrix(y_test, model.predict(X_test))
cm_display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['purple', 'green'])
cm_display.plot()

plt.show()

