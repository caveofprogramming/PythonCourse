#!./venv/bin/python

def main():
    
    numbers = [x for x in range(0,20) if x % 2 == 1]

    print(numbers)

    more_numbers = [2*x if x > 10 else 0 for x in numbers]
    print(more_numbers)
    
    return
    
main()
