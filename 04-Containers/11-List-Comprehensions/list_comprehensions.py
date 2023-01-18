#!./venv/bin/python

def main():
    animals1 = ["dog", "cat", "horse"]

    animals2 = [animal.upper() for animal in animals1]
    print(animals2)

    string_lengths = [len(text) for text in animals1]
    print(string_lengths)

    numbers1 = [1, 2, 3, 4, 5]

    numbers2 = [x*x for x in numbers1]
    print(numbers2)
    
    return
    
main()
