#!./venv/bin/python

import numpy as np

def main():
    values = np.array([1, 2, 3, 4])
    bools = np.array([True, True, False, True])

    print(values[bools])

if __name__ == "__main__":  
    main()
