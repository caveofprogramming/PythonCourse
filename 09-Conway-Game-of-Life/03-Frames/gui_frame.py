#!./venv/bin/python

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.geometry("1200x800")
    root.wm_title("Conway's Game of Life")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=True, ipadx=0, ipady=0)
    canvas.create_rectangle(0, 0, 1200, 800, fill='blue')

    root.mainloop()
    
main()
