#!./venv/bin/python

import re

def main():
    text = "one, two ,three, four"

    fields = re.split(r"\s*,\s*", text)

    print(fields)
    
main()
