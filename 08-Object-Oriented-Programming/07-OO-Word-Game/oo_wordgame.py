#!./venv/bin/python

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
        # Assign self._word to a word randomly chosen from the list of words.

        # Add all the letter of the word (separately) to self._letters
        pass

    def run(self):
        self._choose_word()

def main():
    game = WordGame('peach', 'alligator', 'sky', 'fascinate')
    game.run()
    
main()
