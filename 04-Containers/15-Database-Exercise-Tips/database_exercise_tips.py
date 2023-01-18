#!./venv/bin/python

import os
import sys

"""

CRUD 

Create a program that displays the following menu:

1. Display database
2. Add an item
3. Delete an item
4. Change an item
5. Quit

The program contains a list of items; for example, fruits.

If you select 1, the program displays the items in the list, numbering each item. For example:

0: orange
1: banana
2: blackberry

If you select 2 the program asks you to enter a new item. It adds what you've typed to the list.

If you select 3, the program asks you to enter the list number of an item to delete. It deletes the specified item from the list.

If you select 4,  the program asks you to enter the list number of an item to change, then asks you to enter text. It changes the specified item to the speicified text. 

If you select 5, the program quits.

Until you quit with option 5, the program displays the menu again after every action.

"""

def show_menu():
    pass

def show_database(db):
    pass

def add_item(db):
    pass

def change_item(db):
    pass

def delete_item(db):
    pass

def main():
    db = ["apple", "orange", "mango"]

    show_database(db)

