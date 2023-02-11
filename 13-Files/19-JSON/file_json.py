#!./venv/bin/python

# JSON

from json import dump, load

def main():
    numbers = [1.23, 3.23, 67.232, 10]
    text = "Hello! Fine weather today!"
    lookup = {
        1: "Jan",
        2: "Feb",
        3: "Mar"
    }

    to_save = {
        "values": numbers,
        "greeting": text,
        "months": lookup,
    }

    filename = "data.json"

    with open(filename, 'wt') as file:
        dump(to_save, file)

    with open(filename, 'rt') as file:
        loaded = load(file)

    print(loaded)

if __name__ == "__main__":  
    main()
