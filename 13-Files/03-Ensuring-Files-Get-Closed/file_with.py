#!./venv/bin/python

def main():

    """
    try:
        file = open("mall_customers.csv")
        lines = file.readlines()

        for line in lines:
            print(line, end="")
    finally:
        file.close()
    """
    
    with open("mall_customers.csv") as file:
        lines = file.readlines()

        for line in lines:
            print(line, end="")

if __name__ == "__main__":  
    main()
