#!./venv/bin/python

import numpy as np

def main():
    values1 = np.array([1, 2])
    print(values1)
    print()
    print(np.tile(values1, 3))
    print()
    print(np.tile(values1, [2, 3]))
    print()
    values2 = np.array([1, 2, 3, 4]).reshape(2, 2)
    print(values2)
    print()
    print(np.tile(values2, [3, 2]))


if __name__ == "__main__":  
    main()
