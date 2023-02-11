#!./venv/bin/python

import numpy as np

def variance(data):
    mean = np.mean(data)

    var = 0
    for value in data:
        var += (value - mean)**2

    var /= len(data)
    return var

def main():
   data1 = np.random.randn(3)

   print(data1)

   print(np.var(data1))
   print(np.std(data1))

   print(variance(data1))
   print(variance(data1)**0.5)

if __name__ == "__main__":  
    main()
