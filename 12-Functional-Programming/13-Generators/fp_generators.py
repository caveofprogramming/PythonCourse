#!./venv/bin/python

def main():
    li = [chr(x) for x in range(65, 69)]
    print(li)

    g = (chr(x) for x in range(65, 69))
    print(g)

    for x in g:
        print(x)

    print(list(chr(x) for x in range(65, 69)))
    print(set(chr(x) for x in range(65, 69)))
    print(tuple(chr(x) for x in range(65, 69)))

if __name__ == "__main__":  
    main()
