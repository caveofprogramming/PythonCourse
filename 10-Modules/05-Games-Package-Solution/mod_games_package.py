#!./venv/bin/python

import games.game_of_life as gol
import games.wordgame as wordgame

def main():
    app = wordgame.App()
    app.run()

if __name__ == '__main__':
    main()