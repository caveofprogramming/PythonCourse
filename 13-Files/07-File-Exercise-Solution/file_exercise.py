#!./venv/bin/python

data = """
Apples
Eggs
Milk
Onions
"""

def main():
    filename = "temp.txt"

    with open(filename, 'wt') as file:
        file.write(data)

    items = list()

    """
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            items.append(line)
   

    with open(filename, 'rt') as file:
        items = [x.strip() for x in file if x.strip()]

    """

    with open(filename, 'rt') as file:
        items = list(filter(lambda x: x, map(lambda x: x.strip(), file)))

    print(items)

if __name__ == "__main__":  
    main()
