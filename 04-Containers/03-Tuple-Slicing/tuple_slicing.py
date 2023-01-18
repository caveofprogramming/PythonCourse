#!./venv/bin/python

def main():
    animals = ("goat", "sheep", "dog", "elephant")

    print(animals[1])
    print(animals[1:3])
    print(animals[0:3])
    print()
    print(animals[-1])
    print(animals[-3:-1])

    extract = animals[0:2]

    print(extract)

    text = "It was the best of times"
    print()
    print(text[3])
    print(text[0:6])


    
main()
