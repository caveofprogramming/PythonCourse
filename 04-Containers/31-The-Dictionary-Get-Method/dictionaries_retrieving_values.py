fruits = {
    "apple": "green",
    "orange": "orange",
    "banana": "yellow",
}

color = fruits.get("mango")

print(color)
print(type(color))

color = fruits.get("mango", "red")
print(color)

color = fruits.get("banana", "red")
print(color)
