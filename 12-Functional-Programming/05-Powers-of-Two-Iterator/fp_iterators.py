
class PowersOfTwo:

    def __init__(self, max):
        self._max = max

    def __iter__(self):

        self._index = 0
        self._last_value = 1
        return self

    def __next__(self):

        self._index += 1

        result = self._last_value

        self._last_value *= 2

        if self._index > self._max:
            raise StopIteration

        return result

pot = PowersOfTwo(5)

for x, y in enumerate(pot):
    print(x, y)

print()

for x, y in enumerate(pot):
    print(x, y)