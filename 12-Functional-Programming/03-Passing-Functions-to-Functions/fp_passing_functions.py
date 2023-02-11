#!./venv/bin/python

def double(n):
    return n * 2

def apply(values, f):

    result = []

    for value in values:
        result.append(f(value))

    return result

def main():
    numbers = [2, 3, 4, 6, 10]

    result = apply(numbers, double)

    print(result)

if __name__ == "__main__":  
    main()
