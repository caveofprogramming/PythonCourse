#!./venv/bin/python

import numpy as np

def main():
    num = np.arange(16).reshape(4,4)

    print(num)
    print()
    print(num[0,:])
    print(num[:,0])
    print()
    print(num)
    print()
    
    num_view = num[::3,::3]

    num_view += 1000
    print(num_view)
    print()
    print(num)

if __name__ == "__main__":  
    main()
