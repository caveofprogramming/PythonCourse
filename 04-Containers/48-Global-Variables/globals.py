#!./venv/bin/python

value = 0

def do_something():
    global value
    print(value)
    value = 10
    print(value)

def main():
   do_something()

   print(value)

main()