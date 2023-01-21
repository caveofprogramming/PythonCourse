

fruits1 = {
    "apple": "green",
    "orange": "orange",
    "banana": "yellow",
}

fruits2 = fruits1.copy()
fruits1.pop("apple")
print(fruits1)
print(fruits2)

fruits3 = {key:value for (key, value) in fruits2.items()}
print(fruits3)