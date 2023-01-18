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

    options = ("Display the database", "Add an item", "Delete an item", "Change an item", "Quit")
    
    print()
    for i in range(0, len(options)):
        print(str(i + 1) + ": " + options[i])
    print()

def show_database(db):
    print()
    for i in range(0, len(db)):
        print(str(i) + ": " + db[i])
    print()

def add_item(db):
    item = input("Enter item to add: ")
    db.append(item)

def change_item(db):
    item_number = input("Enter number of item to change: ")
    item = input("Enter new item: ")

    db[int(item_number)] = item

def delete_item(db):
    item_number = input("Enter number of item to delete: ")
    db.pop(int(item_number))

def main():
    db = ["apple", "orange", "mango"]

    do_loop = True

    while do_loop:
        show_menu()

        option = input("select option > ")

        if option == "1":
            show_database(db)
        elif option == "2":
            add_item(db)
        elif option == "3":
            delete_item(db)
        elif option == "4":
            change_item(db)
        elif option == "5":
            do_loop = False
        else:
            print("Unrecognised option")

main()

