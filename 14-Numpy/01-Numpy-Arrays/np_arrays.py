#!./venv/bin/python

import numpy as np

def main():
    num1 = np.array([1, 2, 3, 4], dtype='int16')

    print(num1)

    print(num1.dtype)
    print(num1.ndim)
    print(num1.shape)
    print(num1.nbytes)

    num2 = np.array([[1, 2], [3, 4], [5, 6]])
    print()
    print(num2)
    print(num2.shape)

if __name__ == "__main__":  
    main()
