#!./venv/bin/python

class Animal:
    def eat(self):
        print("I am eating")

    def speak(self):
        print("I am an animal")

class Cat(Animal):
     def speak(self):
        print("I am a cat")

def main():
    cat1 = Cat()

    cat1.eat()
    cat1.speak()
    
main()
