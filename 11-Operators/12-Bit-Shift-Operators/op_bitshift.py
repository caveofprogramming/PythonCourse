#!./venv/bin/python

def printb(value):
    print(f"{value & 0b11111111:08b}")

def main():
    pass

if __name__ == "__main__":  
    num1 = 0b10001000

    printb(num1)
    
    printb(num1 >> 1)
    printb(num1 >> 4)

    num1 >>= 2

    printb(num1)

    print(10 >> 1)

    print()
    num1 = 0b01001001
    printb(num1)
    printb(num1 << 2)

    print(10 << 3)
