#!./venv/bin/python

def number_range():
    for i in range(0, 5):
        yield i

def main():
    
    for i in number_range():
        print(i)

"""
    for x in powers_of_two(5):
        print(x)
"""

if __name__ == "__main__":  
    main()
