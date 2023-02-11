#!./venv/bin/python

def main():
    data = (0x123456).to_bytes(3, 'big')

    print(type(data))
    print(f'{data[0]: x}')
    print(f'{data[1]: x}')
    print(f'{data[2]: x}')

    print(data)

if __name__ == "__main__":  
    main()
