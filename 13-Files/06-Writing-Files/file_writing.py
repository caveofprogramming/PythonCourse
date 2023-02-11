#!./venv/bin/python

"""
Apples
Eggs
Milk
Onions
"""

def main():
    with open("temp.txt", 'w') as file:
        file.write("Hello\n")
        file.write("Bob\n")

    print("Running")

if __name__ == "__main__":  
    main()
