#!/usr/bin/env python3
# write_csv.py
# write a CSV file

import csv
CSV_FILE = "averages.csv"

def main():
    avg_list = [['Smith', 'John', '89'],
                ['Jones','Sally', 98],['Green','Rashad', 93]]
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)   # create a CSV writer
        for row in avg_list:        # for each row in list
            writer.writerow(row)    # write comma-delimited values

main()
