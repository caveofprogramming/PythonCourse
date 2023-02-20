from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import numpy as np

plt.style.use('dark_background')

def plot(X, y):
    fig, ax = plt.subplots(figsize=(16,9))
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="terrain")
    plt.show()

def plot_nearest_neighbor_info(X):
    X = StandardScaler().fit_transform(X)
    model = NearestNeighbors(n_neighbors=4)
    model.fit(X)
    distances, _ = model.kneighbors()
    sorted_distances = np.sort(distances, axis=0)

    fig, ax = plt.subplots(figsize=(16,9))
    ax.plot(sorted_distances[:, 3])
    ax.axhline(y=0.150, linestyle='dashed')
    plt.show()

def dbscan(X):
    X = StandardScaler().fit_transform(X)
    model = DBSCAN(eps=0.3, min_samples=4)
    return model.fit_predict(X)

def main():
    X, _ = make_moons(n_samples=200, noise=0.05, random_state=0)

    y_clusters = dbscan(X)
    plot(X, y_clusters)
    #plot_nearest_neighbor_info(X)

main()