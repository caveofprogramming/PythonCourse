#!./venv/bin/python

def main():
    numbers1 = {1, 2, 3}
    print(numbers1)

    numbers1.add(7)
    numbers1.add(9)
    print(numbers1)

    numbers2 = {10, 20, 30}

    numbers1.update(numbers2)
    print(numbers1)

    numbers1.update(["cat", "dog"])
    print(numbers1)
    
main()
