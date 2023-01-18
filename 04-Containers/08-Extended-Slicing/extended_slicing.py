numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven"]

print(numbers[3:7:2])

numbers[3:7:2] = ["hello", "hi"]
print(numbers)

print(numbers[::])

greeting = "Hello there"
print(greeting[::2])

print("What are you?"[3::3])