#!./venv/bin/python

from array import array

def main():
    numbers = array('f', [-8, 123.0, 0.0001, 87.5, 1.23456789])
    NUMBER_ITEMS = len(numbers)

    filename = "numbers.bin"

    with open(filename, 'wb') as file:
        numbers.tofile(file)

    del numbers

    with open(filename, 'rb') as file:
        numbers = array('f')
        numbers.fromfile(file, NUMBER_ITEMS)

    print(numbers)


    print("Finished.")

if __name__ == "__main__":  
    main()
