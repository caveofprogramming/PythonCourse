#!./venv/bin/python

from collections import defaultdict

def create_word_stats_file(input_file, output_file):

    counts = defaultdict(int)

    with open(input_file, 'rt') as file:
        for line in file:
            (word, count) = line.split(',')
            word = word.strip()
            count = count.strip()
            counts[len(word)] += int(count)

    maxlen = max(counts.keys())

    with open(output_file, 'wt') as file:
        for i in range(1, maxlen + 1):
            count = counts[i]
            print("%d,%d" %  (i,count), file=file)

def main():
    create_word_stats_file('wordcounts.txt', 'wordlengths.csv')

if __name__ == "__main__":  
    main()
