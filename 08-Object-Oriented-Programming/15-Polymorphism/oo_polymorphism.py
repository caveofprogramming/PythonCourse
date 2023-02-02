#!./venv/bin/python

class Animal:
    def eat(self):
        print("Animal eating")

    def speak(self):
        print("I'm an animal")

class Cat(Animal):
    def speak(self):
        print("I'm a cat")

def main():
    cat1 = Cat()
    cat1.speak()
    cat1.eat()
    
main()
