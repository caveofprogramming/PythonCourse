#!./venv/bin/python

"""
Assign sequential IDs to 'Machine' objects, so machines have an ID
1, 2, 3, 4 etc. in the order they are created.
"""

class Machine:

    count = 0

    def __init__(self):
        Machine.count += 1
        self._id = Machine.count

    def get_id(self):
        return self._id

def main():
    m1 = Machine()
    m2 = Machine()
    m3 = Machine()

    print(m2.get_id())
    print(Machine.count)
    
main()
