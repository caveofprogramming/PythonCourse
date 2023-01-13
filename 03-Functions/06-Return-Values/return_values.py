def greet(name):
    print("Hello " + name)

def create_greeting(name):
    return "Hi " + name

def create_simple_greeting():
    return "Hi there!"

def main():
    name = "John"
    greet(name)

    greeting = create_greeting(name)
    print(greeting)

    simple_greeting = create_simple_greeting()
    print(simple_greeting)

main()