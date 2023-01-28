#!./venv/bin/python

def main():
    name = "Zoe"
    text = "Hello %s. How are you?" % name
    print(text)

    print("Hello %s and %s. How are you today?" % ("Zoe", "Jack"))
    print("Hello %s. The temperature is %d " % ("Zoe", 31))
    print("Hello %s. The temperature is %f " % ("Zoe", 31.1234))
    print("Hello %s. The temperature is %.2f " % ("Zoe", 31.1234))
    print("Hello %s. The temperature is %10d " % ("Zoe", 31))
    print("Floating point in a width of 10: %10.1f" % 1.2345)


main()
