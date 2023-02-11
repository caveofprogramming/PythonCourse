#!./venv/bin/python

import re

def main():

    pattern = re.compile(r'([a-zà-ÿ][a-zà-ÿ’]*)', flags=re.I)
    
    with open('text1.txt', 'rt') as file:
        for line in file:
            words = re.findall(pattern, line)

            for word in words:
                print(word)

if __name__ == "__main__":  
    main()
