def greet(name):
    print(id(name))
    print("Hello " + name)

def main():
    name = "John"

    print(id(name))
    greet(name)

main()