#!./venv/bin/python

import games
import sys

def main():
    print(dir(games.data))

    games.data.loader.load()

    #print(sys.path)

if __name__ == "__main__":  
    main()
