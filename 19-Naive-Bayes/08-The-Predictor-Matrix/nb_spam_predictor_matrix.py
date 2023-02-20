import re
from collections import defaultdict

def load():

    emails = []

    with open('spam_ham_dataset.csv', 'rt') as file:
        for line in file:
            m = re.match(r'\d+,(spam|ham),(.*)', line)

            if(m):
                spam = m.group(1) == 'spam'
                subject = m.group(2)
                emails.append({'spam': spam, 'text':subject})
            elif len(emails) > 0:
                emails[-1]['text'] += line

    return emails

def get_common_words(emails):
    frequencies = defaultdict(int)

    for email in emails:
        counts = get_counts(email['text'])

        for word, count in counts.items():
            frequencies[word] += count

    words = dict(sorted(frequencies.items(), reverse=True, key=lambda item: item[1]))
    common_words = list(words.keys())[:10]

    return common_words

def get_counts(text):
    frequencies = defaultdict(int)

    words = re.findall(r'\w+', text)

    for word in words:
        frequencies[word] += 1

    return frequencies

def get_frequencies(emails, words):
    frequencies = []

    for email in emails:
        counts = get_counts(email['text'])
        row = list(map(lambda word: counts[word], words))
        frequencies.append(row)

    return frequencies


def main():
    emails = load()
   
    words = get_common_words(emails)

    X = get_frequencies(emails, words)

    print(X)

main()