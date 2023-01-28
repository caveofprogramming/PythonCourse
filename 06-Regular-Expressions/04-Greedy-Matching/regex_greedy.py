#!./venv/bin/python

import re

def main():
    text = "zigzag"
    result = re.match("z.*g", text)
    print("No match" if result is None else f"Match: {result.group()}")

    text = "zigzag"
    result = re.match("z.*?g", text)
    print("No match" if result is None else f"Match: {result.group()}")

    text = "zigzag"
    result = re.match("z.*?", text)
    print("No match" if result is None else f"Match: {result.group()}")

    text = "zigzag"
    result = re.match("z.*?$", text)
    print("No match" if result is None else f"Match: {result.group()}")
    
main()
