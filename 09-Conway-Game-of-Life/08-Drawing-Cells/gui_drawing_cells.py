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

class GameCanvas(tk.Canvas):
    def __init__(self, frame):
        super().__init__(frame, borderwidth=0, highlightthickness=0)

    def draw(self):

        cell_size = 57
        cols = self.winfo_width() // cell_size
        rows = self.winfo_height() // cell_size

        for row in range(0, rows):
            for col in range(0, cols):
                x = col * cell_size
                y = row * cell_size

                id = self.create_rectangle(x, y, x + cell_size, y + cell_size, outline='gray', fill='black')

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
