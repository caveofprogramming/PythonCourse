class Cat:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def introduce(self):
        print(f"Hello, my name is {self._name}. I weigh {self._weight:.1f} Kg")

def main():
    cat1 = Cat("Ruffles", 1.2)
    cat2 = Cat("Tiddles", 1.8)

    cat1.introduce()
    cat2.introduce()

main()

