#!./venv/bin/python

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.wm_title("Conway's Game of Life")

class MainFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)
        canvas = tk.Canvas(self)
        canvas.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)
        canvas.create_rectangle(0, 0, 1200, 800, fill='blue')


def main():
    app = App()
    MainFrame(app)
    app.mainloop()
    
main()
