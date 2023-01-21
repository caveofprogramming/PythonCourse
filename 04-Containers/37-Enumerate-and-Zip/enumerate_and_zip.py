
fruits = ["apple", "orange", "banana"]
animals = ["dog", "cat", "goat"]

for i, item in enumerate(fruits):
    print(i, item)

print()

for fruit, animal in zip(fruits, animals):
    print(fruit, animal)