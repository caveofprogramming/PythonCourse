#!./venv/bin/python

"""
Write a function that converts feet to miles.

(miles = feet x 1.89E-4)

Using this function, write a program that asks the user to enter a distance in feet and converts it to miles.

If the user enters valid input, print the distance in miles to three decimal places and quit.
If the user enters invalid input, print "Invalid input" and ask them again.

If the user enters "quit", quit the program.


Mount Everest is 29,028 feet high. How high is it in miles?

"""

def feet_to_miles(feet):
    return feet * 1.89E-4

def main():
    
    while True:
        feet = input("Enter distance in feet > ")

        if feet == "quit":
            break

        try:
            feet = feet.replace(",", "")
            miles = feet_to_miles(int(feet))
            print(f"{feet} is equivalent to {miles:.3f} miles")
            break
        except:
            print("Invalid input.")
    
main()
