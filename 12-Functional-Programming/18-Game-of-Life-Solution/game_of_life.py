#!./venv/bin/python

import tkinter as tk
from tkinter import ttk
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.wm_title("Conway's Game of Life")
        self.resizable(False, False)
        self._frame = MainFrame(self)

    def run(self):
        self.update()
        self._frame.update()
        self.mainloop()

class Cell:
    _canvas = None

    @classmethod
    def set_canvas(cls, canvas):
        Cell._canvas = canvas

    def __init__(self, id):
        self._id = id
        self._active = False
        self._canvas.tag_bind(id, "<Button-1>", self._on_click)
        self._next_state = False

    def flip(self):
        self.set_state(self._next_state)

    def get_state(self):
        return self._active

    def _on_click(self, event):
        self.set_state(not self._active)

    def set_next_state(self, state):
        self._next_state = state

    def set_state(self, state):
        self._active = state
        self._canvas.itemconfig(self._id, fill='green' if self._active else 'black')

    def __str__(self):
        return f'ID: {self._id}'

class GameCanvas(tk.Canvas):
    def __init__(self, frame):
        super().__init__(frame, borderwidth=0, highlightthickness=0)

        Cell.set_canvas(self)
        self._cells = list()
        self._rows = 0
        self._cols = 0

    def randomise(self):

        for _ in range(0, 400):
            row = random.choice(self._cells)
            cell = random.choice(row)
            cell.set_state(True)

    def clear(self):
        for row in self._cells:
            for cell in row:
                cell.set_state(False)

    def next(self):

        """
        If cell is live and has 2 or 3 live neighbours, it remains alive.
        If cell is dead and has 3 live neighbours, it becomes alive.
        Otherwise the cell dies
        """

        for row in range(0, len(self._cells)):
            for col in range(0, len(self._cells[row])):
                cell = self._cells[row][col]
                live_neighbours = self._get_live_neighbours(row, col)

                next_state = False

                if cell.get_state():
                    if live_neighbours == 2 or live_neighbours == 3:
                        next_state = True
                else:
                    if live_neighbours == 3:
                        next_state = True

                cell.set_next_state(next_state)

        for row in self._cells:
            for cell in row:
                cell.flip()

    def _get_live_neighbours(self, row, col):

        count = 0

        gen = ((rowoffs, coloffs) 
            for rowoffs in range(-1, 2) for coloffs in range(-1, 2) 
            if not (rowoffs == 0 and coloffs == 0))

        for rowoffs, coloffs in gen:
                rowpos = (row + rowoffs) % self._rows
                colpos = (col + coloffs) % self._cols

                cell = self._cells[rowpos][colpos]
                count += cell.get_state()

        return count

    def draw(self):

        cell_size = 20
        self._cols = self.winfo_width() // cell_size
        self._rows = self.winfo_height() // cell_size
        margin_x = (self.winfo_width() % cell_size)/2
        margin_y = (self.winfo_height() % cell_size)/2

        for row in range(0, self._rows):

            row_list = list()
            self._cells.append(row_list)

            for col in range(0, self._cols):
                x = col * cell_size + margin_x
                y = row * cell_size + margin_y

                id = self.create_rectangle(x, y, x + cell_size, y + cell_size, outline='gray', fill='black')
                row_list.append(Cell(id))

class MainFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2000)
        self.rowconfigure(0, weight=2000)
        self.rowconfigure(1, weight=1)

        canvas = GameCanvas(self)
        canvas.grid(column=0, row=0, columnspan=3, sticky='NSEW', padx=5, pady=3)
        self._canvas = canvas

        next_button = ttk.Button(self, text="Step", command=canvas.next)
        next_button.grid(column=0, row=1, sticky=tk.W, padx=5, pady=1)

        clear_button = ttk.Button(self, text="Clear", command=canvas.clear)
        clear_button.grid(column=1, row=1, sticky=tk.W, padx=5, pady=1)

        random_button = ttk.Button(self, text="Randomise", command=canvas.randomise)
        random_button.grid(column=2, row=1, sticky=tk.W, padx=5, pady=1)

       

    def update(self):
        self._canvas.draw()

def main():
    print(__name__)
    app = App()
    app.run()
    
if __name__ == '__main__':
    main()
