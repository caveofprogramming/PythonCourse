#!./venv/bin/python

def main():
    file = open("mall_customers.csv")

    lines = file.readlines()

    for line in lines:
        print(line, end="")

    file.close()

if __name__ == "__main__":  
    main()
