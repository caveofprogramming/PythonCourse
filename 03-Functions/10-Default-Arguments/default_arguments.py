
def new_patient(name, type = "cat", age = -1):
    print(name, type, age)

def main():
    new_patient("Biffy", "dog", 5)
    new_patient("Tiddles", "cat")
    new_patient("Rover", "dog", 8)
    new_patient("Bobby")

main()