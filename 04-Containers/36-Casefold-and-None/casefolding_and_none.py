
NAME = "Oscar"
name = "oscar"

print(NAME.casefold() == name.casefold())

print("Abcß".casefold())

names = {"Bob": 45}

age = names.get("Jim")
print(age)

if age is None:
    print("Name not found")