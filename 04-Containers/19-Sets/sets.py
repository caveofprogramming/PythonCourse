
numbers = {1, 2, 3, 1}

print(numbers)

numbers_list = [2, 3, 3, 2, 5, 6]
print(set(numbers_list))

for number in numbers:
    print(number)

print(3 in numbers)
print(5 in numbers)

"""
list: ordered, "in" is slow, mutable
tuple: ordered, "in" is slow. immutable
set: not ordered, "in" is fast, mutable
"""