#!/usr/bin/env python3

# file_reader3.py
# opens, reads, and prints a file
# which contains digits of pi

FILENAME = 'phonetic.txt'

with open(FILENAME) as f:
    for line in f:
       print(line.rstrip())

