"""
volume = width * height * length
"""

def calculate_box_volume(width, height, length):
    return width * height * length

def main():
    volume = calculate_box_volume(5, 2, 10)

    print("Box volume is:", volume)

main()