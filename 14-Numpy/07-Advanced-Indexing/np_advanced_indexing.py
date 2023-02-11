#!./venv/bin/python

import numpy as np

def main():
    num = np.arange(16).reshape(4,4)

    print(num)

    values = num[[1,2,3],[0,1,3]]

    print(values)

    print(num[num % 2 == 0])
    print(num[num < 5])



if __name__ == "__main__":  
    main()
