#!./venv/bin/python

import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(-15, 15, 200)
    y = np.sin(x)

    plt.figure(figsize=(16, 9))
    plt.axis([-16, 16, -2, 2])
    plt.plot(x, y, "--", color="darkblue")
    plt.rc('axes', titlesize=18)
    plt.title("y = sin(x)")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

if __name__ == "__main__":  
    main()
