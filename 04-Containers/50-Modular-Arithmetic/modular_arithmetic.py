#!./venv/bin/python

"""
Clock
5 + 12 = 5 = 17 - 12
7 + 13 = 8 
"""

def main():
    print( (7 + 12) % 12)

    for i in range(0, 30):
        print(i % 12, end=" ")
    
    animals = ["dog", "cat", "cow"]

    for i in range(0, 30):
        animal = animals[i % len(animals)]
        print(animal, end=", ")
main()
