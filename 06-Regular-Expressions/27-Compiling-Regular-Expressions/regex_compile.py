#!./venv/bin/python

import re

def main():
    text = "Oranges are nice"

    regex = re.compile(r"o\w+s", flags=re.I)

    print(re.sub(regex, "Bananas", text))
    
main()
