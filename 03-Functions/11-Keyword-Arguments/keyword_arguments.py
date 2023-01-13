#!./venv/bin/python

def new_fruit(color, weight, sweetness, location):
    print(color)
    print(weight)
    print(sweetness)
    print(location)

def main():
    new_fruit("orange", 1, 60, "Colombia")
    print()
    new_fruit(color="red", sweetness=40, weight=0.5, location="Namibia")
    
main()
