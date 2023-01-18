#!./venv/bin/python

"""
Print all the cubic numbers up to and including 729
Print all the square numbers up to and including 729

Which cubic numbers are also square numbers?
Which cubic numbers are not square numbers?
"""

def main():
    # x**3 is x*x*x
    cubic_set = {x**3 for x in range(10)}
    print(cubic_set)

    # x**2 is x*x
    square_set = {x**2 for x in range(28)}
    print(max(square_set))

    print(cubic_set.intersection(square_set))
    print(cubic_set - square_set)
    
main()
