#!./venv/bin/python

import re

class IdException(Exception):
    pass

class Machine:
    def __init__(self, name, id):
        self._name = name
        self._id = id

        if re.search(r"\d", self._id) is None:
            raise IdException("Machine ID contains no number")


    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}"

    def get_name(self):
        return self._name

    def set_id(self, id):
        self._id = id

class Car(Machine):
    pass

def main():
    car1 = Car("Herbie", "abc1")

    print(car1.get_name())
    print(car1)
    
main()
