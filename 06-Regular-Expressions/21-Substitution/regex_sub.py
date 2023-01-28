#!./venv/bin/python

import re

def main():
    text = "Hello Jack. How are you, Jack?"

    text = re.sub(r"J\w+", "Zoe", text)

    print(text)

main()
