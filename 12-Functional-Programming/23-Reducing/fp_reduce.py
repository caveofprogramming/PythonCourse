#!./venv/bin/python

from functools import reduce
from operator import add

def main():
    numbers = [1, 2, 3, 4, 5]

    print(reduce(lambda x, y: x + y, numbers))
    print(reduce(add, numbers))

if __name__ == "__main__":  
    main()
