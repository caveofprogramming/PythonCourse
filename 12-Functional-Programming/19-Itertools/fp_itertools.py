#!./venv/bin/python

import itertools as it

def main():
    items = it.product(range(-1, 2), range(-1, 2))
    items = it.filterfalse(lambda v: v[0]==0 and v[1]==0, items)

    for x, y in items:
        print(x, y)

if __name__ == "__main__":  
    main()
