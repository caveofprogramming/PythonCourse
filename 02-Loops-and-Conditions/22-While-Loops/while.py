#!./venv/bin/python

PASSWORD = "hello123"

password = ""

while password != PASSWORD:
    password = input("Enter your password: ")

print("Access granted.")