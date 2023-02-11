#!./venv/bin/python

import numpy as np

def main():
    m1 = np.arange(0,4).reshape(2,2)
    m2 = np.arange(1,5).reshape(2,2)

    print(m1)
    print()
    print(m2)

    print()
    print(m1 + m2)
    print()
    print(3 * m1)

    m3 = np.arange(0,2)
    print()
    print(m1)
    print(m3)
    print()
    print(m1 + m3)

if __name__ == "__main__":  
    main()
