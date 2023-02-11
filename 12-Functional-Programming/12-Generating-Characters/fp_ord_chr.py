#!./venv/bin/python

def main():
    print(ord('A'))
    print(chr(65))

    letters = [chr(x) for x in range(ord('A'), ord('E'))]

    print(letters)

if __name__ == "__main__":  
    main()
