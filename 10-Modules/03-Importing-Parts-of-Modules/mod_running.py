#!./venv/bin/python

from game_of_life import App, Cell

def main():
    app = App()
    app.run()

    cell = Cell(5)
    
if __name__ == '__main__':
    main()
