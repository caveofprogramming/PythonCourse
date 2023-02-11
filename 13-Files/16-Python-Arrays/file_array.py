#!./venv/bin/python

from array import array

def main():
    numbers = array('f', [-8, 123.0, 0.0001, 87.5])

    print(numbers)

    print(f'{9.999999747378752e-05: f}')

    print(numbers.tolist())
    print(numbers.tobytes())

if __name__ == "__main__":  
    main()
