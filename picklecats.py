#!/usr/bin/env python3

# picklecats.py
# write and read data to a binary file

import pickle   # module for working with binary files
FILENAME = "kittens.bin"

# 3x2 list of kittens and ages (in years)
kittens = [["Snowball", 5],
           ["Mr. Snuffles", 3],
           ["Fluffy", 7]]

# write the list to a file
with open(FILENAME, "wb") as file:  # write binary
    pickle.dump(kittens, file)

# read the file into a list and print
with open(FILENAME , "rb") as file: # read binary
    kitten_list = pickle.load(file)
    print(kitten_list)
