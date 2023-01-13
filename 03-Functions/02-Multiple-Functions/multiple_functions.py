PASSWORD = "hello"

def greeting():
    print("Welcome! No unauthorised users.")

def check_password():
    password = input("Enter your password > ")

    if password == PASSWORD:
        print("Access granted.")
    else:
        print("Access denied.")

def main():
    greeting()
    check_password()

main()



