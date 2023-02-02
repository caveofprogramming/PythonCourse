#!./venv/bin/python

class Person:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self._age

    def set_age(self, age):

        if age < 0 or age > 125:
            raise ValueError(f"Age {age} is out of range")
        self._age = age

    age = property(fget=get_age, fset=set_age)

def main():
    p1 = Person(40)

    p1.age = 20

    print(p1.get_age())

    
main()
