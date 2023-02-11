#!./venv/bin/python

import tkinter as tk
from tkinter import filedialog

def save():
    file_path = filedialog.asksaveasfilename(initialfile="test.txt")
    print(file_path)

def open():
    file_path = filedialog.askopenfilename(initialfile="test.txt")
    print(file_path)

def main():
    root = tk.Tk()
    root.geometry("800x600")

    menubar = tk.Menu(root)
    root.config(menu=menubar)

    file_menu = tk.Menu(menubar)
    menubar.add_cascade(label="File", menu=file_menu)

    file_menu.add_command(label="Open", command=open)
    file_menu.add_command(label="Save", command=save)

    root.mainloop()


if __name__ == "__main__":  
    main()
