#!./venv/bin/python

def main():
    data = (0x123456).to_bytes(3, 'big')

    value = int.from_bytes(data, 'big')

    print(hex(value))

    

    

if __name__ == "__main__":  
    main()
