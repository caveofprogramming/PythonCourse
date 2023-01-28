#!./venv/bin/python

import re

def main():
    email = "john@caveofprogramming.com"

    result = re.match("\w{2,30}@\w{2,40}\.\w{2,10}", email)

    print("No match" if result is None else "Match")


main()