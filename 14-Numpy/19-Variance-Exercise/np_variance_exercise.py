#!./venv/bin/python

import numpy as np

"""
Show that the average value of the variance of small samples actually improves if we use n-1 in the variance formula instead of n

Show that duplicating entries in an array of random values doesn't change the variance if we add duplicate values to the array.

How does variance change if we multiply the entries in a random array by a scalar? How does standard deviation change?

In a (large) array of normally-distributed values with a variance of 1 and a mean of 0, what percentage of the values lie between -1 and 1?
"""

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
