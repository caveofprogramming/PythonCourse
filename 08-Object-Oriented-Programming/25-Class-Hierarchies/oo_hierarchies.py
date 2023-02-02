#!./venv/bin/python

class Animal:
    pass

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Tiger(Cat):
    def speak(self):
        print("Growl")

class SiberianTiger(Tiger):
    pass

def main():
    print(SiberianTiger.mro())
    
main()
