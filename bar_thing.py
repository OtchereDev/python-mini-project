import pprint
import sys
from collections import defaultdict

texts='Like the castle in its corner in a medieval game, I foresee \
    terrible trouble and I stay here just the same.'

Alphabets='abcdefghijklmnopqrstuvwxyz'

mapped=defaultdict(list)

for text in texts:
    text=text.lower()
    if text in Alphabets:
        mapped[text].append(text)


print("\nYou may need to stretch console window if text wrapping occurs.\n") 
print("text = ",end='') 
print("{}\n".format(text),file=sys.stderr)
pprint.pprint(mapped,width=110)

