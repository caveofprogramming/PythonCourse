#!./venv/bin/python

CORRECT_PASSWORD = "hello123"

correct = False

for i in range(0, 3):
    password = input("Enter your password: ")

    if(password == CORRECT_PASSWORD):
        correct = True
        break
    else:
        print("Incorrect password.")

if correct:
    print("Greetings Professor Falcon")
else:
    print("Access denied.")







