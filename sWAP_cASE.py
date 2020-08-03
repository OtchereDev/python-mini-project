import re

word='HackerRank.com presents "Pythonist 2"'

def swap_case(s):
    new=''
    for i in s:
        
        if i.isupper():
            i= i.lower()
            new += i
        else:
            i = i.upper()
            new += i

    s = new
    return s

print(swap_case('HackerRank.com presents "Pythonist 2"'))