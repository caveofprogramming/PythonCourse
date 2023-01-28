#!./venv/bin/python

import re

def main():
    text = "drooooool"

    result = re.match("dr.*l", text)

    if result is None:
        print("No match")
    else:
        print(result.group())


main()