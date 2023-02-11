#!./venv/bin/python

import matplotlib.pyplot as plt
import numpy as np

def main():
    fig = plt.figure()
    ax = fig.add_subplot(211, projection="3d")

    x = np.random.randn(1000)
    y = np.random.randn(1000)
    z = np.random.randn(1000)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.scatter(x, y, z)

    ax = fig.add_subplot(212, projection="3d")

    z = np.linspace(0, 20, 1000)
    x = np.cos(z)
    y = np.sin(z)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot(x, y, z)

    plt.show()

if __name__ == "__main__":  
    main()
