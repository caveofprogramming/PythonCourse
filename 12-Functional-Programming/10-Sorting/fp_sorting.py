#!./venv/bin/python

def main():
    animals = ['dog', 'elephant', 'cat', 'giraffe', 'badger']

    animals1 = sorted(animals, reverse=True, key=lambda item: len(item))

    print(animals1)

    animals.sort(reverse=True, key=lambda item: len(item))
    print(animals)

if __name__ == "__main__":  
    main()
