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

    var /= (len(data) - 1)
    return var

def main():

    variances = []
    stddevs = []

    for i in range(0, 10000):
        values = np.random.randn(10)
        var = variance(values)
        variances.append(var)
        stddevs.append(var**0.5)

    print(np.mean(variances))
    print(np.mean(stddevs))

   

if __name__ == "__main__":  
    main()
