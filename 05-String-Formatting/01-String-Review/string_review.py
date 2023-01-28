"""
- concatenation
- print multiple arguments
- string methods: lower, upper, casefold, join
- print termination character
- control characters / escape sequences: \n \t \\ 
"""

print("Hello " + "there")
print("Hello " + str(7))
print("Hello", 100, {1, 2, 3}, 1.23)

print("Hello".upper())
print("Hello".casefold())
print(", ".join({"one", "two", "three"}))
print("Hello", end="....")
print("Hi")
print()
print("Hi,\nhow\nare\tyou\\")
print('"Hi"')
print("'Hi'")
print("Hello \"Bob\"")