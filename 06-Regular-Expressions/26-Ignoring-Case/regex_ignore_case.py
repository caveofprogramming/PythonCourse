#!./venv/bin/python

import re

def main():
    text = "Hello Bob"

    print(re.match(r".*bob", text, re.IGNORECASE))

    print(re.sub(r"bob", "Zoe", text, flags=re.IGNORECASE))
    
main()
