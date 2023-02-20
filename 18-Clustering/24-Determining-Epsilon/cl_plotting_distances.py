import numpy as np
from math import cos, sin, pi
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

class WeirdClusters:
    def __init__(self):
        x = []
        y = []

        for i in np.arange(0, 2*pi, 0.01):
            r = np.random.uniform(90, 100)
            x.append(r * cos(i))
            y.append(r * sin(i))

        for i in range(0, 100, 1):
            x.append(np.random.normal(0, 10))
            y.append(np.random.normal(0, 10))

        self._x = np.array(x).reshape(-1, 1)
        self._y = np.array(y).reshape(-1, 1)
        self._X = np.append(self._x, self._y, axis=1)

    def plot(self):
        fig = plt.figure(figsize=(9, 9))
        ax = fig.add_subplot()
        ax.scatter(self._x, self._y)
        plt.show()

    def plot_neighbor_distances(self):
        nn = NearestNeighbors(n_neighbors=4)
        nn.fit(self._X)

        # NB: scale/normalise the data is necessary first!!!

        distances, indices = nn.kneighbors()
        sorted_distances = np.sort(distances, axis=0)
        
        fig = plt.figure(figsize=(16,9))
        ax = fig.add_subplot()
        ax.set_xlabel("Sample number")
        ax.set_ylabel("Distance to furthest nearest neighbor")
        ax.plot(sorted_distances[:,3])
        ax.axhline(y=6, linestyle='dashed')
        plt.show()

def main():
    w = WeirdClusters()
    #w.plot()
    w.plot_neighbor_distances()

main()