#!./venv/bin/python

class Machine:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}"

    def get_name(self):
        return self._name

    def set_id(self, id):
        self._id = id

def main():
    m = Machine("THX1138", 1234)

    name = m.get_name()
    name = "Karloff"

    m.set_id(5678)

    print(m)


    
main()
