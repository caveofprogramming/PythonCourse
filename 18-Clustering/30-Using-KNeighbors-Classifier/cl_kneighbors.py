from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split
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

def classify_by_neighbours(X_train, y_train, X_test):

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)

    return model.predict(X_test)

def main():
    X, _ = make_moons(n_samples=300, noise=0.05, random_state=0)

    X_train, X_test = train_test_split(X, train_size=0.7, shuffle=True)

    y_clusters = dbscan(X_train)

    y_predicted = classify_by_neighbours(X_train, y_clusters, X_test)
    plot(X_test, y_predicted)
    #plot_nearest_neighbor_info(X)

    print(silhouette_score(X_train, y_clusters))

main()