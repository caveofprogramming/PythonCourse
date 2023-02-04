#!./venv/bin/python

def printb(value):
    print(f"{255 & value:08b}")

def main():
    num1 = 0b10001000
    num2 = 0b00001001

    printb(num1)
    printb(num2)
    printb(num1 ^ num2)

    print(True != False)

    printb(~num1)

if __name__ == "__main__":  
   main()
