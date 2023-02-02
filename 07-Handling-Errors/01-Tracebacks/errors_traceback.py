#!./venv/bin/python

def greet():
    print("Hello")
    print(1/0)

def main():
    greet()
    
main()
