#!/usr/bin/python3

def multiple_returns(sentence):
    # If the sentence is empty, return (0, None)
    if len(sentence) == 0:
        return (0, None)
    else:
        # Return a tuple with the length of the string and its first character
        return (len(sentence), sentence[0])
