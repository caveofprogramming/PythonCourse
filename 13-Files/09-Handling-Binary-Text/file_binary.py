#!./venv/bin/python

# bytearray
# bytes
# ő
# ASCII unicode

def main():
    data = bytearray([1, 7, 2, 100, 255, 0xFF])
    print(list(data))

    data = bytearray("Hello", 'utf8')
    print(list(data))

    print(b"Hello")
    data = bytearray(b'Hello')
    print(list(data))

    data = bytearray("ő", 'utf8')
    print(list(data))

    print(ord('ő'))
    print(chr(337))

if __name__ == "__main__":  
    main()
