#!./venv/bin/python

"""
Procedural programming (PP) - functions calling functions
Object-oriented programming (OOP) - classes and objects
Functional programming (FP) -- passing functions to functions
"""

class Person:
    def eat(self):
        print("I'm eating!")

    def talk(self):
        print("Hello!")

def main():
   person1 = Person()
   person2 = Person()

   person1.talk()
   person2.eat()
    
main()
