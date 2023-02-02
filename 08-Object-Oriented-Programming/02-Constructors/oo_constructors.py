#!./venv/bin/python

"""
Procedural programming (PP) - functions calling functions
Object-oriented programming (OOP) - classes and objects
Functional programming (FP) -- passing functions to functions
"""

class Person:

    def __init__(self, name):
        print(f"{name} created!")

    def eat(self):
        print("I'm eating!")

    def talk(self):
        print("Hello!")

def main():
   person1 = Person("Zoe")
   person2 = Person("Zara")
   person3 = Person("Zach")

   person1.talk()
   person2.eat()
    
main()
