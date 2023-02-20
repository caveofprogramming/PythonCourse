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

def get_counts(text):
    frequencies = defaultdict(int)

    words = re.findall(r'\w+', text)

    for word in words:
        frequencies[word] += 1

    return frequencies

def main():
    emails = load()
   
    for email in emails:
        print(get_counts(email['text']))

main()