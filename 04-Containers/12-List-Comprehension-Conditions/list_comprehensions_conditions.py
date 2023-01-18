#!./venv/bin/python

def main():

    numbers1 = [x for x in range(0, 10)]
    print(numbers1)

    numbers2 = [x for x in numbers1 if x > 5]
    print(numbers2)

    numbers3 = [x for x in numbers1 if x % 2 == 0]
    print(numbers3)

    # Mod operator
    print(13 % 5)

    print(18 % 2 == 0)

    
main()
