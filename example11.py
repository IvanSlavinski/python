"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even
indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just
explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to
start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there
are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
"""


def to_weird_case(string):
    string = [list(x) for x in string.split()]
    new_string = []
    for x in string:
        y = []
        counter = 0
        for j in x:
            if counter % 2 == 0:
                y.append(j.upper())
                counter += 1
            else:
                y.append((j.lower()))
                counter += 1
        new_string.append(y)
    new_string = ["".join(x) for x in new_string]
    return " ".join(new_string)