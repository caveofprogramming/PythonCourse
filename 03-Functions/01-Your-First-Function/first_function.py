"""
Procedural: C
Object-Oriented: Java
Functional: Haskell
"""

def ask_user_status():
    response = input("How are you? : ")

    if response == "OK" or response == "ok":
        print("Excellent!")
    else:
        print("Oh no.")

ask_user_status()
