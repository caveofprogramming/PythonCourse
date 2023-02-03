#!./venv/bin/python

import random
import re

class WordGame:
    def __init__(self, *words):

        # List of possible words
        self._words = words

        # Set of correctly-guessed letters
        self._guesses = set()

        # Set of all letters in the word
        self._letters = set()

        # Number of guesses made by the user
        self._number_guesses = 0

        self._word = None

    def _choose_word(self):
        self._word = random.choice(self._words)
        self._letters.update(self._word)

    def _guess_letter(self):
        text = input("Guess a letter > ")

        if len(text) == 0:
            return

        letter = text[0]

        if letter in self._word:
            self._guesses.add(letter)

        self._number_guesses += 1

    def _show_word(self):
        regex = f'[^0{"".join(self._guesses)}]'
        text = re.sub(regex, '-', self._word)
        text = re.sub(r"(.)", r" \1 ", text)
        print(text)

    def _display_result(self):
        print(f"\nGuessed '{self._word}' in {self._number_guesses} guesses.")
        

    def run(self):
        self._choose_word()

        while self._guesses != self._letters:
            self._show_word()
            self._guess_letter()

        self._display_result()

class App:
    def run(self):
        game = WordGame('peach', 'alligator', 'sky', 'fascinate')
        game.run()

def main():
    app = App()
    app.run()
    
if __name__ == '__main__':
    main()
