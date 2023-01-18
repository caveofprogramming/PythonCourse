#!./venv/bin/python

def main():

    animals = ["dog", "donkey", "duck"]

    animals.insert(1, "giraffe")

    print(animals)

    more_animals = ["elephant", "monkey"]

    animals.extend(more_animals)

    print(animals)
    return
    
main()
