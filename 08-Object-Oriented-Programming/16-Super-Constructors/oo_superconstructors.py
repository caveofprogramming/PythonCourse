#!./venv/bin/python

class Machine:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        print("Car constructor")

class Car(Machine):
    def __init__(self, id, name, type):

        #Machine.__init__(self, id, name)
        super().__init__(id, name)
        self._type = type

    def __str__(self):
        return f'{self._id}: {self._name}'

def main():
   car1 = Car(1234, "Herbie", "Jaguar")

   print(car1)
    
main()
