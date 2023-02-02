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

        canvas = tk.Canvas(self)
        canvas.create_rectangle(0, 0, 1200, 800, fill='blue')
        canvas.grid(column=0, row=0, columnspan=2, sticky='NSEW', padx=5, pady=3)


def main():
    app = App()
    MainFrame(app)
    app.mainloop()
    
main()
