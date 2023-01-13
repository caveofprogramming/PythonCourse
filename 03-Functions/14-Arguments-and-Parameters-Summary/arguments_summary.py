#!./venv/bin/python

"""
Exercise: define a single function that accepts:
    one or more positional arguments
    zero or more variable arguments
    zero or more variable keyword arguments

    Make the function print out all arguments it receives.
"""

def positional_arguments(one, two, three):
    print(one)
    print(two)
    print(three)

def default_arguments(one, two=2, three=3):
    print(one)
    print(two)
    print(three)

def variable_arguments(*args):
    for arg in args:
        print(arg)

def variable_keyword_arguments(**kwargs):
    for key in kwargs:
        print(key + " -- " + str(kwargs[key]))

def main():

    # 1. Positional arguments
    positional_arguments(1, 2, 3)
    print()

    # 2. Default arguments
    default_arguments(2)
    print()

    # 3. Keyword arguments
    positional_arguments(one="Hello", two="there", three="professor")
    print()

    # 4. Variable arguments
    variable_arguments("orange", "banana", "apple", 1, 2, 3)
    print()

    # 5. Variable keyword arguments
    variable_keyword_arguments(speed=90, color="red", size="big")



    return
    
main()
