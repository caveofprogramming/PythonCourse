#!./venv/bin/python

import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.pie([1, 2, 3, 4], labels=[1, 2, 3, 4], colors=['green', '#FF8800', (0,0,1), (0,0.5,1)], explode=[0, 0, 0, 0.1], autopct='%.1f %%')
    plt.title("Some Stuff")
    plt.legend()
    plt.show()

if __name__ == "__main__":  
    main()
