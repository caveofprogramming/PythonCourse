#!./venv/bin/python

def main():
    numbers1 = {1, 2, 3, 4, 5, 6, 7}
    numbers2 = {8, 0, 3, 10, 3, 6, 1}

    numbers1.difference_update(numbers2)
    print(numbers1)

    print(numbers1.issuperset(numbers2))

    print({1, 2, 3}.issuperset({1, 2}))

    
main()
