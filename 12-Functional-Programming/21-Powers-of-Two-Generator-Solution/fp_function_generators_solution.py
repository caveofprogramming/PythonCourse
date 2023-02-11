#!./venv/bin/python

def powers_of_two(n):
    powers = 1
    for _ in range(0, n):
        yield powers
        powers *= 2

def main():
    for x in powers_of_two(5):
        print(x)

if __name__ == "__main__":  
    main()
