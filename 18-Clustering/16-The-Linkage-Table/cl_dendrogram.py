from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = np.array([0, 1, 2, 12]).reshape(-1, 1)

X = StandardScaler().fit_transform(data)

clusters = linkage(X)

print(X)
print(clusters)

dendrogram(clusters)

plt.show()