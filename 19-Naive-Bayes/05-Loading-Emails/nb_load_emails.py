import re

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

def main():
    emails = load()
    print(emails)

main()