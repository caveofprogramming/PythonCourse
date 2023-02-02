#!./venv/bin/python

def do_greet():
    raise ZeroDivisionError("Not a real key error!")
    greet()

def greet():
    print("Hello")
    print(1/0)

def main():

    try:
        while True:
            print("Hello")
        do_greet()
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except KeyError as ke:
        print(f"Key error: {ke}")
    except KeyboardInterrupt:
        print("Keyboard interrupt: program ending.")
    except Exception as e:
        print(f"General error: {e}")
    
    
main()
