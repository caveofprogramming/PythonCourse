#!./venv/bin/python

def do_greet():
    d = dict()
    print(d['hello'])
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
    except:
        print("Some unknown error occurred")
    
    
main()
