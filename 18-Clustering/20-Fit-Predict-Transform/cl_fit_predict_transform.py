import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import sklearn.datasets as ds

data = ds.load_iris(as_frame=True)
df = data['data']
y = data['target']
X = df.iloc[:,0:1]

# No predict method
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
# or
X = scaler.fit_transform(X)

# No transform method
logistic = LogisticRegression()
logistic.fit(X, y)
predicted = logistic.predict(X)

# Transform method exists
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
clusters = kmeans.predict(X)

# predict() and transform() methods do not exist
agglom = AgglomerativeClustering(n_clusters=3)
agglom.fit(X)
clusters = agglom.fit_predict(X)

