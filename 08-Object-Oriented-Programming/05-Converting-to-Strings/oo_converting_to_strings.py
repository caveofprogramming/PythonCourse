#!./venv/bin/python

class Cat:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __str__(self):
        return f"Name: {self._name}\n\tWeight: {self._weight}"

    def introduce(self):
        print(f"Hello, my name is {self._name}. I weigh {self._weight:.1f} Kg")

def main():
    cat1 = Cat("Ruffles", 1.2)
    cat2 = Cat("Tiddles", 1.8)

    cat1.introduce()
    cat2.introduce()

    cat_string1 = str(cat1)
    print(cat_string1)

    print(cat2)
    
main()
