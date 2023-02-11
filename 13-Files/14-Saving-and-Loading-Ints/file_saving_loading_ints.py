#!./venv/bin/python

def main():
    numbers = [12, 34239479, 9, 444]
    filename = "numbers.dat"

    with open(filename, 'wb') as file:
        for number in numbers:
            file.write(number.to_bytes(4, 'big'))

    numbers_from_file = list()

    with open(filename, 'rb') as file:
        for i in range (0, len(numbers)):
            data = file.read(4)
            number = int.from_bytes(data, 'big')
            numbers_from_file.append(number)

    print(numbers_from_file)

if __name__ == "__main__":  
    main()
