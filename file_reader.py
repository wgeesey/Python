#!/usr/bin/env python3

# file_reader.py
# opens, reads, and prints a file
# which contains digits of pi

FILENAME = 'pi_digits.txt'

with open(FILENAME) as f:
    contents = f.read()
print(contents)
