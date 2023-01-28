#!./venv/bin/python

import re

def main():

    text = """
    1. Apple
    2. Orange
    3. Cherries
    4. Strawberries
    """
    
    result = re.findall(r"(\d+)\.\s+(\w+)", text)

    print(result)
    
main()
