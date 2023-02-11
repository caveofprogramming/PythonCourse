#!./venv/bin/python

def main():
    seq = filter(lambda x: x % 2 == 0, (x for x in range(0, 20)))

    print(list(seq))

if __name__ == "__main__":  
    main()
