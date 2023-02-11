#!./venv/bin/python

def main():
    print([x for x in range(0, 3)])
    print([x for x in range(0, 3) if x != 1])
    print(['*' if x == 0 else x for x in range(0, 3)])

if __name__ == "__main__":  
    main()
