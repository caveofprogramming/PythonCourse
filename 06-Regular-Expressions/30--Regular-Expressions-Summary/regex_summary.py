#!./venv/bin/python

import re

def main():
    """
    .   Wildcard
    \s  space
    \S  non-space
    \w  number, letter, underscore
    \W  Not number, letter or underscore
    \d  Digit
    \D  Not digit
    \n  Newline
    \r\f    Carriage return and form feed

    []  Character class, matches one of several characters
    ()  Group
    (?: )  Not a group; used just for removing ambiguity
    (?=)    Zero-width positive lookahead assertion
    (?!)    Zero-width negative lookahead assertion
    |   Alternatives

    re.I    ignore case
    re.M    Multiline; make ^ and $ match start and end of lines, not strings
    re.DOTALL   Make . match newlines
    search
    match
    fullmatch

    *   Match zero or more of the preceeding; greedy
    *?  Match zero or more of the preceeding; non-greedy
    +   Match one or more of the preceeding; greedy
    +?  Match one or more of the preceeding; non-greedy

    split
    sub
    findall
    """

    text = "apple orange banana"

    print(re.search("orange", text))
    print(re.match("apple", text))
    print(re.fullmatch("apple orange banana", text))
    
main()
