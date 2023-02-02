#!./venv/bin/python

import random

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
        # Display the word, BUT:

        # For any letters that aren't guessed yet, display '-'
        # For any letters that have been guessed by now, display the letter
        # Space out all the letters and hyphens; NOT --a--d-, but - - a - - d -
        pass
        

    def run(self):
        self._show_word()
        self._choose_word()
        self._guess_letter()
        self._show_word()
        self._guess_letter()
        self._show_word()

def main():
    game = WordGame('peach', 'alligator', 'sky', 'fascinate')
    game.run()
    
main()
