#!./venv/bin/python

def main():
    fruits = {
        "apple": "green",
        "orange": "orange",
        "banana": "yellow",
    }

    keys = fruits.keys()
    values = fruits.values()
    items = fruits.items()

    print(keys)
    print(values)
    print(items)

    keys_list = list(keys)

    print(keys_list)

    fruits["raspberry"] = "red"

    print()
    print(keys)
    print(keys_list)


main()