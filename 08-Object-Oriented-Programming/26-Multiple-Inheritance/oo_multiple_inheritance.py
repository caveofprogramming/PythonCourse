#!./venv/bin/python

class Camera:
    def take_photo(self):
        print("Taking photo.")

class Phone:
    def make_call(self):
        print("Making call.")

class SmartPhone(Camera,Phone):
    pass

def main():
    device = SmartPhone()

    device.make_call()
    device.take_photo()
    
main()
