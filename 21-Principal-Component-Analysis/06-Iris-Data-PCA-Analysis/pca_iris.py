from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn

iris = load_iris(as_frame=True)
X = iris['data']
y = np.choose(iris['target'], iris['target_names'])

pca = PCA(2)
components = pca.fit_transform(X)

fig, ax = plt.subplots()
ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
sn.scatterplot(x=components[:,0], y=components[:,1], hue=y, palette='husl', ax=ax)

plt.show()
