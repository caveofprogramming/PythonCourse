#!./venv/bin/python

"""
        Device
    Camera      Phone
        Smartphone
"""

class Device:
    def activate(self):
        print("Device activated")

class Camera(Device):
    def activate(self):
        print("Camera activated")

    def take_photo(self):
        print("Taking photo.")

class Phone(Device):
    def make_call(self):
        print("Making call.")

class SmartPhone(Camera,Phone):
    pass

def main():
    device = SmartPhone()

    device.make_call()
    device.take_photo()

    print(SmartPhone.mro())

    device.activate()
    
main()
