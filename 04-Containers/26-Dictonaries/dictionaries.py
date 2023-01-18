#!./venv/bin/python

def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
        True: 7
    }

    print(fruits["apple"])
    print(fruits["orange"])
    print(fruits["banana"])
    print(fruits[True])

main()