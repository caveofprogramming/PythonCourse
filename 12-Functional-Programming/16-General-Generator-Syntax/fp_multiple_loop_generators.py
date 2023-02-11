#!./venv/bin/python

def main():
    print(list((x,y) if x != y else '=' for x in range(0,4) if x != 1 for y in range(0,4) if y != 2))

if __name__ == "__main__":  
    main()
