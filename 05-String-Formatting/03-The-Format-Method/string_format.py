#!./venv/bin/python

def main():
    print("Hello {}".format("Zoe"))
    print("Hello {1} and {0}".format("Zoe", "Jack"))
    print("The temperature is {}".format(11))
    print("The temperature is {:.2f}".format(31.2345))
    print("We have {number_units} units available.".format(number_units=98))
    print("Hello {name}. It is {temperature:.1f} degrees today".format(temperature=27.123, name="Jack"))

    print()

    print("It is {distance:,.0f} miles to the sun".format(distance=9.3E7))

    print("Hello {:>20}".format("Zoe"))

    print("We have {:.1%} fuel left".format(0.25))
    
main()
