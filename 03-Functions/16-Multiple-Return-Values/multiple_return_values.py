#!./venv/bin/python

def get_user_info():
    name = input("Enter your name > ")
    height = input("Enter your height > ")

    return name, height

def main():
    name, height = get_user_info()

    print(name + ": " + height)
    
main()
