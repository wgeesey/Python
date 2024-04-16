#!/usr/bin/env python3
# json_number_reader.py
# JSON number reader, from Matthes Crash Course 2e

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)
