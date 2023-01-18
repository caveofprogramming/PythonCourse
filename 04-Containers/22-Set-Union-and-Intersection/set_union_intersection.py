#!./venv/bin/python

def main():
    numbers1 = {1, 2, 3, 4, 5, 6, 7}
    numbers2 = {8, 0, 3, 10, 3, 6, 1}

    print(numbers1.union(numbers2))
    print(numbers1.intersection(numbers2))

    print("Difference")
    print(numbers1.difference(numbers2))
    print(numbers1 - numbers2)
    print(numbers2.difference(numbers1))

    print(numbers2.symmetric_difference(numbers1))
    
main()
