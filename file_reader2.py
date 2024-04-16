#!/usr/bin/env python3

# file_reader2.py
# opens, reads, and prints a file
# which contains digits of pi

FILENAME = 'phonetic.txt'

with open(FILENAME) as f:
    lines = f.readlines() #reads the file into a python list

#print(lines)

for line in lines:
#   print(line)
   print(line.rstrip())
