import re
from collections import defaultdict
from sklearn.naive_bayes import ComplementNB, GaussianNB, MultinomialNB, BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt

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
    common_words = list(words.keys())[:1000]

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
    y = [email['spam'] for email in emails]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, train_size=0.7)

    model = BernoulliNB()
    model.fit(X_train, y_train)

    y_predicted = model.predict(X_test)

    print(model.__class__)
    print(accuracy_score(y_test, y_predicted))
    cm = confusion_matrix(y_test, y_predicted)
    ConfusionMatrixDisplay(cm).plot()

    plt.show()



main()