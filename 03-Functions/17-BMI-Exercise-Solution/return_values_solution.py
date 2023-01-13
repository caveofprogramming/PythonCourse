#!./venv/bin/python

"""
Write a function that asks the user to enter their weight in kilos
and their height in metres, then calculatues their BMI

(weight divided by height times height)

The function should return all three values.
"""

def calculate_bmi():
    height = input("Enter height in metres: ")
    weight = input("Enter weight in kilos: ")

    bmi = float(weight)/(float(height) * float(height))

    return weight, height, bmi

def main():
    weight, height, bmi = calculate_bmi()

    print("Weight: " + str(weight))
    print("Height: " + str(height))
    print("BMI: " + str(bmi))
    
main()
