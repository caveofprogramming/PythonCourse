#!./venv/bin/python

import games.game_of_life

def main():
    app = games.game_of_life.App()
    app.run()

if __name__ == '__main__':
    main()