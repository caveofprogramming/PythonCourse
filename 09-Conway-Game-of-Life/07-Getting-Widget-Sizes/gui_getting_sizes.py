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
        print(self.winfo_width())
        print(self.winfo_height())
        self.create_rectangle(10, 10, 800, 600, outline='red', fill='blue')

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
