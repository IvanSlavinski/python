"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    list_sentence = sentence.split()
    reversed_sentence = []
    for word in list_sentence:
        if len(word) >= 5:
            word = word[::-1]
            reversed_sentence.append(word)
        else:
            word = word
            reversed_sentence.append(word)
    sentence = " ".join(reversed_sentence)
    return sentence