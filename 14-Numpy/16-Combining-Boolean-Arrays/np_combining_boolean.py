#!./venv/bin/python

import numpy as np

def main():
    v1 = np.array([True, True, False, False])
    v2 = np.array([True, False, True, False])

    print(v1)
    print(v2)
    print()
    print(v1 & v2)
    print(v1 | v2)
    print(v1 ^ v2)

if __name__ == "__main__":  
    main()
