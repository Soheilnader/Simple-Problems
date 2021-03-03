import string

def is_pangram(sentence):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    lst = []
    for i in sentence.lower():
        if i in alpha:
            lst.append(i)
    if len(set(lst)) == 26:
        return True
    else:
        return False
