#!./venv/bin/python

class Clock:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        display_value = self._value % 12

        if display_value == 0:
            display_value = 12

        return f"{display_value} {'am' if (self._value % 24) < 12 else 'pm'}"

def main():
    c1 = Clock(7)    # 7 am
    c2 = Clock(19)   # 7 pm    
    c3 = Clock(0)    # 12 am
    c4 = Clock(12)   # 12 pm 
    c5 = Clock(25)   # 12 pm 

    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print(c5)


if __name__ == "__main__":  
    main()
