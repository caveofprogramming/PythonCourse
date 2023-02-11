#!./venv/bin/python

import matplotlib.pyplot as plt

def main():

    NWORDS = 10
    counts = []
    labels = []

    with open('wordcounts.txt', 'rt') as file:
        for i, line in enumerate(file):
            (word, count) = map(lambda item: item.strip(), line.split(','))
            counts.append(int(count))
            labels.append(word)

            if i == NWORDS - 1:
                break

    plt.figure(figsize=(16,9))
    plt.pie(counts, labels=labels, autopct='%.1f')
    plt.title('Word Counts in Great Expectations')
    plt.show()
    
if __name__ == "__main__":  
    main()
