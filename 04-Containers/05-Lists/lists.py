#!./venv/bin/python

def main():
    fruits = ["apple", "orange", "banana"]

    print(len(fruits))

    print(fruits[2])
    print(fruits[0:2])

    test1 = tuple()
    test2 = list()

    animals = ("fox", "rabbit")
    print(animals)
    animals = list(animals)
    print(animals)

    for animal in animals:
        print(animal)
    
main()
