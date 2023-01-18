#!./venv/bin/python

def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    for fruit in fruits:
        print(fruit + ": " + fruits[fruit])

    print()

    for fruit in fruits.keys():
        print(fruit + ": " + fruits[fruit])


    print("apple" in fruits)

    print()

    for (fruit, color) in fruits.items():
        print(fruit + ", " + color)

    print()

    for fruit in fruits.values():
        print(fruit)



main()