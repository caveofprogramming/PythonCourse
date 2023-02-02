#!./venv/bin/python

class Widget:

    count = 0

    def __init__(self, name):
        self._name = name

        Widget.count += 1

        print(f"{Widget.count} widgets created.")

    def __str__(self):
        return self._name

def main():
    widget1 = Widget("Project panel")
    widget2 = Widget("Terminal view")

    print(widget1)
    print(widget2)

    print(Widget.count)

    
    
main()
