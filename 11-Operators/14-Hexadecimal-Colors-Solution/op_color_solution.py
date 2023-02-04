#!./venv/bin/python

"""
red     0x12
green   0x34
blue    0x56

0x123456 (combined colour)

Write a function that accepts three colors: red, green and blue.
The function returns a single combined number containing all three colours

to_color(red, green, blue)

Write a function that accept a color and splits it into red, green and blue components

from_color(color):
    # do something
    return red, blue, green

"""

def to_color(red, green, blue):
    return blue + (green << 8) + (red << 16)

def from_color(color):
    red = (color & 0xFF0000) >> 16
    green = (color & 0x00FF00) >> 8
    blue = (color & 0x0000FF)

    return red, green, blue

def main():
    color = 0x123456

    (red, green, blue) = from_color(color)

    print(f"{red:x} {green:x} {blue:x}")

    combined = to_color(red, green, blue)

    print(f"{combined:x}")

if __name__ == "__main__":  
    main()
