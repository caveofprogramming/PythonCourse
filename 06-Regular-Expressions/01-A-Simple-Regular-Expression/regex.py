#!./venv/bin/python

import re

def main():
    text = "dig"

    result = re.match("d.g", text)

    print(result is not None)
    
main()
