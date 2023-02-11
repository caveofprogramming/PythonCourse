#!./venv/bin/python

import numpy as np

def main():
    m1 = np.array([5, 10, 3, 6]).reshape(2,2)
    m2 = np.array([25, 1, 3, 0.5]).reshape(2,2)

    print(m1)
    print(m2)

    m3 = np.matmul(m1, m2)

    print(m3)


if __name__ == "__main__":  
    main()
