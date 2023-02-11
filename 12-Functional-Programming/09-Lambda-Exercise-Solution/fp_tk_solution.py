#!./venv/bin/python

import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.geometry("400x200")

    label = ttk.Label(root, text="Hello")
    label.pack()

    for i in range(0, 5):
        button = ttk.Button(root, text=str(i), command=lambda i=i: label.config(text=str(i)))
        button.pack()

    root.mainloop()

if __name__ == "__main__":  
    main()
