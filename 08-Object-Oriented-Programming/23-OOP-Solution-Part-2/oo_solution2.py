#!./venv/bin/python

"""
Create a class called Media.
Create the following subclasses: Book, Movie, Podcast

Each subclass should contain instance variables appropriate to the type of media, and should be convertible to a string which displays this information.

Create several instances of each class and add them to a container.

Write a program that displays a prompt, like this:

search >

When the user enters a word or phrase, the program searches all Media objects to find a match in their details. If any matches are found, it displays them.

If no matches are found, it prints "No match".

If the user types "quit", the program terminates. Otherwise it displays the prompt again.
"""


class Media:
    def __init__(self, title):
        self._title = title

    def search_str(self):
        fields = vars(self)
        return " ".join(fields.values())


class Book(Media):
    def __init__(self, title, author):
        super().__init__(title)
        self._author = author

    def __str__(self):
        return f"Title: {self._title}\nAuthor: {self._author}"


class Movie(Media):
    def __init__(self, title, director):
        super().__init__(title)
        self._director = director

    def __str__(self):
        return f"Title: {self._title}\nDirector: {self._director}"


class Podcast(Media):
    def __init__(self, title, episode):
        super().__init__(title)
        self._episode = episode

    def __str__(self):
        return f"Title: {self._title}\nEpisode: {self._episode}"


def main():
    media = [
        Book("Journey to the Centre of the Earth", "Jules Verne"),
        Book("Moby Dick", "Herman Melville."),
        Book("A Tale of Two Cities", "Charles Dickens"),
        Movie("Limitless", "Neil Burger"),
        Movie("Withnail and I", "Bruce Robinson"),
        Podcast("Cave of Programming Podcast",
                "Episode 1: Why Learn to Code?"),
        Podcast("Skeptiko", "Is the Dalai Lama an Atheist?"),
    ]

    for m in media:
        print(m.search_str())

main()
