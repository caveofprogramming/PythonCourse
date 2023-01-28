#!./venv/bin/python

import re

def main():
    text = """
        one
        two
        three
    """

    print(re.match(r".*two", text, re.DOTALL))

main()
