#!./venv/bin/python

"""
Assign sequential IDs to 'Machine' objects, so machines have an ID
1, 2, 3, 4 etc. in the order they are created.
"""

class Machine:

    _count = 0

    def __init__(self, name):
        Machine._count += 1
        self._id = Machine._count
        self._name = name

    def get_id(self):
        return self._id

    def __str__(self):
        return self._name

    @classmethod
    def create(cls):
        return cls("unknown")

    @classmethod
    def get_count(cls):
        return cls._count

def main():
    m1 = Machine("Camera")
    m2 = Machine("Car")
    m3 = Machine("Coffee machine")

    for x in dir(Machine):
        print(x)

    print(Machine.mro())

    print()

    for x in dir(object):
        print(x)

    print(object.mro())
    
main()
