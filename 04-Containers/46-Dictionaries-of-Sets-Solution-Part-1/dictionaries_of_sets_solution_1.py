#!./venv/bin/python

"""
Put this data in a suitable data structure. 

Science Fiction: Journey to the Centre of the Earth, Day of the Triffids
Drama: A Tale of Two Cities, Moby Dick

Assume:
1. Categories are unique (cannot have two different categories with the same name)
2. Book titles are unique
3. We want to be able to easily determine which books are in a given category.
4. The order of book titles doesn't matter.
5. We want to be able to quickly determine if a given book is present in a given category.
6. We want to be able to easily add books to a category.




Now programmatically add this book:

Science Fiction: The War of the Worlds

Do not assume that the category already exists in the data structure. Write code that will add the book whether the category already exists or not.

Write code that prints all categories and the books in them.

Write a function that can determine whether a particular book is present in the data structure, without knowing the category.
"""

def add_book(library, category, title):

    if not category in library:
        library[category] = set()

    library[category].add(title)


def main():

    library = {
        "Science Fiction": {"Journey to the Centre of the Earth", "Day of the Triffids"},
        "Drama": {"A Tale of Two Cities", "Moby Dick"},
    }

    add_book(library, "Science Fiction", "The War of the Worlds")

    print(library)

main()