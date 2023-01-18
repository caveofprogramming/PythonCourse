
animals1 = ("dog", "cat", "mouse")
animals2 = ("lion", "tiger", "elephant")

fruits1 = ["apple", "orange"]
fruits2 = ["strawberry", "melon", "grape"]

value = 5
# value = value + 3
value += 3
print(value)

print(id(animals1))
animals1 += animals2
print(id(animals1))
print(animals1)

print(id(fruits1))
fruits1 += fruits2
print(id(fruits1))
print(fruits1)