#!./venv/bin/python

from functools import reduce
from operator import add

def main():
    guesses = set('aeiou')
    word = "fascinate"

    # - a - - i - a - e 

    result = reduce(add, map(lambda x: ' - ' if x not in guesses else x, word))
    print(result)

if __name__ == "__main__":  
    main()
