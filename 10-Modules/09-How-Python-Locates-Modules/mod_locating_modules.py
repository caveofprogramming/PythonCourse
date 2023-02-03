#!./venv/bin/python

import sys
import games.game_of_life as gol

def main():
    for dir in sys.path:
        print(dir)

    print(gol.__file__)

if __name__ == "__main__":  
    main()
