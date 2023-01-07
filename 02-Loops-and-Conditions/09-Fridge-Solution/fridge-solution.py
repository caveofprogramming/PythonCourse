# The Fridge

"""

Get the user to enter a temperature in celsius.

< 0: Print "Fridge too cold"
0 - 4: Print "Fridge OK"
4 - 6: Print "Fridge too warm"
> 6: Print "Fridge broken"

"""

temperature = input("Enter the fridge temperature: ")

temperature = float(temperature)

if temperature < 0:
    print("Fridge is too cold.")
elif temperature <= 4:
    print("Fridge OK")
elif temperature < 6:
    print("Fridge too warm")
else:
    print("Fridge is broken.")