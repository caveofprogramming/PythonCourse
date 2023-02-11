#!./venv/bin/python

import numpy as np

def main():
    values = np.arange(-5, 5)

    print(values)

    print(values < 0)

    print(values[values < 0])
    print(values[(values >= -2) & (values <= 2)])

if __name__ == "__main__":  
    main()
