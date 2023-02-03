#!./venv/bin/python

from games import game_of_life as gol, wordgame

def main():

    games = {
        "Game of Life": gol.main,
        "Guess the Word": wordgame.main,
    }

    games["Game of Life"]()

if __name__ == '__main__':
    main()
