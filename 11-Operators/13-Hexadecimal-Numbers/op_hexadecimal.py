#!./venv/bin/python

"""
Hexadecimal

0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 .....

binary b
hexadecimal x
"""

"""
Exercise 1 

Print a table of numbers from 0 to 255.

Print each number in decimal, binary and hexadecimal format
"""

"""
Exercise 2 

red     0x12
green   0x34
blue    0x56

Combined color: 0x123456

Write a function that accepts three colours: red, green and blue. 
The function returns a single integer that combines all three colours, as above.

Write another function that accepts a single combined colour and returns the
red, green and blue components.
"""



def main():
    for i in range(256):
        print(f"{i:03} {i:08b} {i:02x}")

    print("{:6x}".format(0x123456 & 0xFF00FF))

    print("{:6x}".format(0x123456 >> 8))


if __name__ == "__main__":  
    main()
