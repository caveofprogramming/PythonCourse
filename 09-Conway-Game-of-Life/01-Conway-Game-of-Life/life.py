#!./venv/bin/python

import tkinter as tk
from tkinter import ttk

class Cell:

    @classmethod
    def set_canvas(cls, canvas):
        Cell._canvas = canvas

    def _on_click(self, event):
        self._next_state = not self.active
        self.next()

    def __init__(self, id):
        self._id = id
        self.active = False
        self._canvas.tag_bind(id, "<Button-1>", self._on_click)
        self._next_state = False

    def set_next_state(self, state):
        self._next_state = state

    def set_state(self, state):
        self.active = state
        self._canvas.itemconfig(self._id, fill='green' if self.active else 'black')

    def next(self):
        self.set_state(self._next_state)
        

class GameOfLife:
    def __init__(self):
        self._root = tk.Tk()

        width = 1200
        height = 800
        self._root.geometry(f'{width}x{height}')
        frame = MainFrame(width, height)
        self._root.update()
        frame.init()
        frame.draw()

        self._root.bind("<space>", frame._next)

    def run(self):
        self._root.mainloop()

class MainFrame(ttk.Frame):
    def __init__(self, width, height):
        super().__init__()

        self._cell_size = 20

        self.master.title("Conway's Game of Life")
        self.pack(fill=tk.BOTH, expand=1, padx=0, pady=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2000)
        self.rowconfigure(0, weight=2000)
        self.rowconfigure(1, weight=1)

        next_button = ttk.Button(self, text="Step", command=self._next)
        next_button.grid(column=0, row=1, sticky=tk.W, padx=5, pady=1)

        clear_button = ttk.Button(self, text="Clear", command=self._clear)
        clear_button.grid(column=1, row=1, sticky=tk.W, padx=5, pady=1)

        canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        canvas.grid(column=0, row=0, columnspan=2, sticky='NSEW', padx=5, pady=3)

        self._canvas = canvas
        self._grid = list()
        Cell.set_canvas(canvas)
    
    def init(self):
        self._cols = (self._canvas.winfo_width() - 1) // self._cell_size
        self._rows = (self._canvas.winfo_height() - 1)// self._cell_size

        self._endx = self._cols * self._cell_size
        self._endy = self._rows * self._cell_size

    def _clear(self):
        for col in range(0, self._cols):
            for row in range(0, self._rows):
                cell = self._grid[row][col]
                cell.set_state(False)

    def _next(self, *event):
        for col in range(0, self._cols):
            for row in range(0, self._rows):

                cell = self._grid[row][col]

                state = cell.active
                live_neighbours = self._get_live_neighbours(row, col)

                new_state = False

                if state:
                    if live_neighbours == 2 or live_neighbours == 3:
                        new_state = True
                else:
                    if live_neighbours == 3:
                        new_state = True

                cell.set_next_state(new_state)

        for col in range(0, self._cols):
            for row in range(0, self._rows):
                self._grid[row][col].next()

    def _get_live_neighbours(self, row, col):

        count = 0

        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue

                checkRow = (row + x) % self._rows
                checkCol = (col + y) % self._cols
                count += self._grid[checkRow][checkCol].active

        return count    

    def draw(self):
        for row in range(0, self._rows):

            grid_row = list()
            self._grid.append(grid_row)

            for col in range(0, self._cols):
                startx = col * self._cell_size
                starty = row * self._cell_size
                endx = startx + self._cell_size
                endy = starty + self._cell_size

                id = self._canvas.create_rectangle(startx, starty, endx, endy, outline="gray", fill='black')
                grid_row.append(Cell(id))

def main():
    game = GameOfLife()
    game.run()

main()


