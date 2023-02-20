from sklearn.neighbors import NearestNeighbors
import numpy as np

X = np.array([1, 2, 3, 20, 21]).reshape(-1, 1)

model = NearestNeighbors(n_neighbors=3)
model.fit(X)

(distances, indices) = model.kneighbors()

print(indices)