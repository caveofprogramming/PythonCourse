#!./venv/bin/python

def main():
    elements = (True, 3.2, 7, "goat")

    (is_raining, weight, volume, animal) = elements

    print(is_raining)
    print(weight)
    print(volume)
    print(animal)

    fruits = ("apple", "orange", "banana", "strawberry", "pear")

    (fruit1, fruit2, *more_fruits, fruit3) = fruits

    print()
    print(fruit1)
    print(fruit2)
    print(more_fruits)
    print(fruit3)

    print(type(more_fruits))

    one_item = ("goat",)

    print(type(one_item))

    
main()
