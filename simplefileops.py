#!/usr/bin/env python3
# simplefileops.py

FILENAME='simplefileops.txt'

with open(FILENAME, 'w') as f:
    f.write('I love programming.\n')
    f.write('I love creating new games.\n')

with open(FILENAME, 'a') as f:        #append
    f.write('I also find meaning in large datasets.\n')

with open(FILENAME) as f:    # 'r' is implied
    for line in f:
        print(line.replace("\n","")) # replace also removes newlines
