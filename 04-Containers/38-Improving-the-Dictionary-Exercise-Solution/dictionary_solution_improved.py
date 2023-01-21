#!./venv/bin/python


"""
Write a program that asks the user to enter a name.

If the user enters a name in the list below, respond with the age
of the person entered. Otherwise print "Unknown person"

Make the program keep asking for names like this until the user enters
"quit". Then the program exits.

Start by putting the names and ages in a dictionary.
"""

def create_lookup(people, ages):
    lookup = dict()

    for name, age in zip(people, ages):
        lookup[name.casefold()] = age
    
    return lookup

def user_loop(lookup):

    while True:
        user_input = input("Enter a name, or 'quit' > ")

        if user_input == "quit":
            break
        
        age = lookup.get(user_input.casefold())

        if age is None:
            continue

        print(user_input + " is " + str(age) + " years old")

def main():
    people = ["Amelia", "Arthur", "Isla", "Noah", "Ava", "Leo", "Mia", "Oscar"]
    ages = [20, 30, 25, 65, 21, 70, 32, 45]

    lookup = create_lookup(people, ages)

    user_loop(lookup)
main()