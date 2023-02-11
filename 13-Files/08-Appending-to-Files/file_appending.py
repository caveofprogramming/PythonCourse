#!./venv/bin/python

def main():
    with open("temp.txt", 'w') as file:
        file.write("Hello\n")
        file.write("to\n")

    with open("temp.txt", 'a') as file:
        file.write("you\n")

    print("Finished.")

if __name__ == "__main__":  
    main()
