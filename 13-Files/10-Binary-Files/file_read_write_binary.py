#!./venv/bin/python

# serialization: turn data into a series of bytes
# deserialization: turn data series of bytes back into a data type

def main():
    filename = "test.bin"

    data = b'Hello'

    with open(filename, 'wb') as file:
        file.write(data)

    with open(filename, 'rb') as file:
        result = file.read(5)
        print(result)

if __name__ == "__main__":  
    main()
