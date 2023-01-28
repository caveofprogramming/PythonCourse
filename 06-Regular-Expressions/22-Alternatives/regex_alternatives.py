#!./venv/bin/python

import re

def main():
    text = "Hello Jack. Hello Zoe. How are you both doing?"

    text = re.sub(r"Hello (Jack|Zoe|Sam)", r"Hi \1", text)

    print(text)
    
main()
