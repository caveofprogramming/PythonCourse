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

STATUS_BROKEN = "Fridge is broken."
STATUS_OK = "Fridge OK"
STATUS_COLD = "Fridge is too cold."
STATUS_WARM = "Fridge too warm"

status = STATUS_BROKEN

if temperature < 0:
    status = STATUS_COLD
elif temperature <= 4:
    status = STATUS_OK
elif temperature < 6:
    status = STATUS_WARM

print(status)