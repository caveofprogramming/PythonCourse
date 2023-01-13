def greet(name):
    print("Hello " + name)

    print("1. Value of name in greet is: " + name)
    name = "Rachel"
    print("2. Value of name in greet is: " + name)

def main():
    name = "John"

    print("1. Value of name in main is: " + name)
    greet(name)
    print("2. Value of name in main is: " + name)

main()