#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        return
    else:
        return(len(sentence), sentence[0])
