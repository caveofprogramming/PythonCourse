
class PowersOfTwo:

    def __init__(self, max):
        self._max = max

    def __iter__(self):

        self._index = 0
        return self

    def __next__(self):

        self._index += 1
        
        if self._index > self._max:
            raise StopIteration

        return 1

pot = PowersOfTwo(5)

for i in pot:
    print(i)