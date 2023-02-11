#!./venv/bin/python

import numpy as np

def main():
    num = np.linspace(100, 110, 11, dtype=int)
    print(num[1:11:2])
    print(num[:11])
    print(num[1:])
    print(num[::])
    print(num[:8])
    print(num[::2])


if __name__ == "__main__":  
    main()
