#!./venv/bin/python

def main():

    """
    with open("mall_customers.csv") as file:
        while True:
            line = file.readline()

            if not line:
                break

            print(line, end="")
    """

    with open("mall_customers.csv") as file:
       for line in file:
            print(line, end="")

if __name__ == "__main__":  
    main()
