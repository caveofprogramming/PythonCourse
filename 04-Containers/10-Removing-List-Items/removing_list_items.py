#!./venv/bin/python

def main():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    days[0:3] = []

    print(days)

    days.remove("Sat")
    print(days)

    item = days.pop(0)
    print(days)

    print(item)

    del days[1]
    print(days)

    days.clear()
    print(days)

    del days
    # print(days)
    return
    
main()
