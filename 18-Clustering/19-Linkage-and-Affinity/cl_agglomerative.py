import sklearn.datasets as ds
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import normalized_mutual_info_score

"""
linkage / method: ward, complete, average, single
affinity (similarity) / metric: euclidean, cosine
"""

class Iris:
    def __init__(self):
        data = ds.load_iris(as_frame=True)

        self.target = data['target']
        self.names = data['target_names']

        self._df = data['data']
        print(self._df)

    def dendrogram(self):
        X = self._df.iloc[:,0:4]
        X = StandardScaler().fit_transform(X)
        dendrogram(linkage(X, method='complete', metric='cosine'), truncate_mode='level', p=3)
        plt.show()

    def cluster(self):
        X = self._df.iloc[:,0:4]
        X = StandardScaler().fit_transform(X)
        model = AgglomerativeClustering(n_clusters=3, linkage='complete', metric='cosine')
        return model.fit_predict(X)

    def plot(self, clusters):

        xlabel = self._df.columns[2]
        ylabel = self._df.columns[3]
        x = self._df[xlabel]

        fig = plt.figure(figsize=(16,9))

        y = self._df[ylabel]
        ax = fig.add_subplot(121)
        ax.set_title("True Clusters")
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.scatter(x, y, c=self.target, cmap='plasma')

        y = self._df[ylabel]
        ax = fig.add_subplot(122)
        ax.set_title("Calculated Clusters")
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.scatter(x, y, c=clusters, cmap='plasma')

        plt.show()

def main():
    iris = Iris()
    iris.dendrogram()
    clusters = iris.cluster()

    print(clusters)

    print(normalized_mutual_info_score(iris.target, clusters))

    iris.plot(clusters)

main()