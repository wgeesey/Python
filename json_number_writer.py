#!/usr/bin/env python3
# json_number_writer.py
# JSON number writer, from Matthes Crash Course 2e

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
