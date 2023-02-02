#!./venv/bin/python

def do_greet():
    greet()

def greet():
    print("Hello")
    print(1/0)

def main():

    try:
        do_greet()
    except:
        print("Something went wrong!")
    
main()
