# Write your solution here

import string


def separate_characters(my_string):
    letters = ""
    punctuations = ""
    others = ""

    for ch in my_string:
        if ch in string.ascii_letters:
            letters += ch
        elif ch in string.punctuation:
            punctuations += ch
        else:
            others += ch

    return (letters, punctuations, others)
