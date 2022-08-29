#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        ntup = (len(sentence), 'None')
        return ntup
    elif sentence:
        ntup1 = (len(sentence), sentence[0])
        return ntup1
