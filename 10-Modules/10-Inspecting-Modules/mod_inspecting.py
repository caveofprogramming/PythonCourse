#!./venv/bin/python

import sys
import games.game_of_life as gol

def main():

    #value1 = 7
    #print(locals())

    for attr in dir(gol):
        print(attr)

if __name__ == "__main__":  
    main()
