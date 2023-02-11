#!./venv/bin/python

import numpy as np

def main():
    num = np.arange(16).reshape(4,4)

    print(num)
    print()
    print(num[0,:])
    print(num[:,0])


if __name__ == "__main__":  
    main()
