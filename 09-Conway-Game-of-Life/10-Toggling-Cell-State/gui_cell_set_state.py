#!./venv/bin/python

import tkinter as tk
from tkinter import ttk

"""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x                                x
x   x                                x
x   x                                x
x   x                                x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x                                x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.wm_title("Conway's Game of Life")

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

    def _on_click(self, event):
        self.set_state(not self._active)

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

    def draw(self):

        cell_size = 57
        cols = self.winfo_width() // cell_size
        rows = self.winfo_height() // cell_size
        margin_x = (self.winfo_width() % cell_size)/2
        margin_y = (self.winfo_height() % cell_size)/2

        for row in range(0, rows):

            row_list = list()
            self._cells.append(row_list)

            for col in range(0, cols):
                x = col * cell_size + margin_x
                y = row * cell_size + margin_y

                id = self.create_rectangle(x, y, x + cell_size, y + cell_size, outline='gray', fill='black')
                row_list.append(Cell(id))

class MainFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2000)
        self.rowconfigure(0, weight=2000)
        self.rowconfigure(1, weight=1)

        next_button = ttk.Button(self, text="Step")
        next_button.grid(column=0, row=1, sticky=tk.W, padx=5, pady=1)

        clear_button = ttk.Button(self, text="Clear")
        clear_button.grid(column=1, row=1, sticky=tk.W, padx=5, pady=1)

        canvas = GameCanvas(self)
        canvas.grid(column=0, row=0, columnspan=2, sticky='NSEW', padx=5, pady=3)
        self._canvas = canvas

    def update(self):
        self._canvas.draw()

def main():
    app = App()
    app.run()
    
main()
