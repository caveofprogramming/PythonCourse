#!./venv/bin/python

import re
from collections import defaultdict

def main():

    pattern = re.compile(r'([a-zà-ÿ][a-zà-ÿ’]*)', flags=re.I)

    counts = defaultdict(int)
    
    with open('text1.txt', 'rt') as file:
        for line in file:
            words = re.findall(pattern, line)

            for word in words:
                counts[word.lower()] += 1

    counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    with open("wordcounts.txt", 'wt') as file:
        for word, count in counts.items():
            file.write(f'{word},{count}\n')

    print("Written wordcounts.txt")


if __name__ == "__main__":  
    main()
