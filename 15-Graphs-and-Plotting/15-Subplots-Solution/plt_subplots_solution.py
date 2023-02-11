#!./venv/bin/python

import matplotlib.pyplot as plt
import numpy as np

def main():

    fig = plt.figure()
    
    funcs = [
        np.sin, np.cos,
        lambda x: np.sin(x) * np.cos(x), lambda x: x**2,
        lambda x: x**0.5, lambda x: x**np.cos(x)
    ]

    x = np.linspace(0, 20, 1000)

    for i in range(1, 7):
        ax = fig.add_subplot(3, 2, i)
        func = funcs[i - 1]
        y = func(x)
        ax.plot(x, y)

    plt.show()

if __name__ == "__main__":  
    main()
