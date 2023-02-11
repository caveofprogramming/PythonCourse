#!./venv/bin/python

import numpy as np

"""
Show that the average value of the variance of small samples actually improves if we use n-1 in the variance formula instead of n

Show that duplicating entries in an array of random values doesn't change the variance if we add duplicate values to the array.

How does variance change if we multiply the entries in a random array by a scalar? How does standard deviation change?

In a (large) array of normally-distributed values with a variance of 1 and a mean of 0, what percentage of the values lie between -1 and 1?
"""

def main():
    values = np.random.rand(100)

    print(np.std(values))
    print(np.var(values))

    values = np.tile(values, 4)
    std1 = np.std(values)
    var1 = np.var(values)

    values *= 4
    std2 = np.std(values)
    var2 = np.var(values)

    print(std2/std1)
    print(var2/var1)

    values = np.random.randn(100000)
    filtered = values[(values >= -1) & (values <= 1)]

    print(100 * len(filtered)/len(values))

if __name__ == "__main__":  
    main()
