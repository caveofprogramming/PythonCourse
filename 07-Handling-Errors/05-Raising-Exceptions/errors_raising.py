#!./venv/bin/python

def do_greet():
    raise Exception("Not a real key error!")
    greet()

def greet():
    print("Hello")
    print(1/0)

def main():

    try:
        do_greet()
    except ZeroDivisionError as zde:
        print(f"Error: {zde}")
    except KeyError as ke:
        print(f"Key error: {ke}")
    except Exception as e:
        print(f"General error: {e}")
    
main()
