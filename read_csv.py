#!/usr/bin/env python3
# read_csv.py
# read a CSV file

import csv
CSV_FILE = "averages.csv"

def main():
    avg_list = []
    with open(CSV_FILE) as file:
        reader = csv.reader(file)   # create a CSV reader
        for row in reader:          # read each row
            avg_list.append(row)    # append to list

    for row in avg_list:            # display list
        print(row)

main()
