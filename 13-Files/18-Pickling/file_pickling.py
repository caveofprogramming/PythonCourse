#!./venv/bin/python

from pickle import dump, load

def main():
    numbers = [1.23, 3.23, 67.232, 10]
    text = "Hello! Fine weather today!"
    lookup = {
        1: "Jan",
        2: "Feb",
        3: "Mar"
    }

    filename = "data.bin"

    with open(filename, 'wb') as file:
        dump(numbers, file)
        dump(text, file)
        dump(lookup, file)

    del numbers
    del text
    del lookup

    with open(filename, 'rb') as file:
        numbers = load(file)
        text = load(file)
        lookup = load(file)

    print(numbers)
    print(text)
    print(lookup)

if __name__ == "__main__":  
    main()
