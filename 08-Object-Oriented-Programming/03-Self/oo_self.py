#!./venv/bin/python

"""
Procedural programming (PP) - functions calling functions
Object-oriented programming (OOP) - classes and objects
Functional programming (FP) -- passing functions to functions
"""

class Person:

    def __init__(self, name):

        self._name = name
        print(f"{self._name} created!")
        print(id(self))

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

   print(id(person1))
   print(id(person2))
   print(id(person3))

   person1.age = 50
   person2.age = 20

   print(person1.age)
   print(person2.age)

   print(person1._name)
   print(person2._name)
   print(person3._name)

    
main()
