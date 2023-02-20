from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

plt.style.use('dark_background')

def plot(X):
    fig, ax = plt.subplots(figsize=(16,9))
    ax.scatter(X[:, 0], X[:, 1])
    plt.show()

def main():
    X, _ = make_moons(n_samples=200, noise=0.05, random_state=0)

    plot(X)

main()