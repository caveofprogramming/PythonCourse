#!./venv/bin/python

import numpy as np

def main():
    num = np.arange(10)
    print(num)

    num = np.arange(10)
    print(num * 3)
    print(num + 2)
    print(num ** 2)

    print(np.sin(num))
    print(np.max(num))
    print(np.mean(num))
    print(np.std(num))
    print(np.var(num))


if __name__ == "__main__":  
    main()
