import sys
import os

if len(sys.argv) != 2:
    
    print(f'Usage: {sys.argv[0]} input_file')
    sys.exit(1)  # 1 indicates error


print(f'Opening file {sys.argv[1]}.')

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], 'r')

# Input files should contain two integers on separate lines

print('Reading two integers.')
num1 = int(f.readline())
num2 = int(f.readline())


print(f'Closing file {sys.argv[1]}')
f.close()  # Done with the file, so close it


print(f'\nnum1: {num1}')

print(f'num2: {num2}')

print(f'num1 + num2: {num1 + num2}')
--------------------------------------------------------------------

import csv

with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        print(f'Row #{row_num}: {row}')
        row_num += 1
------------------------------------------------------------

import csv

# Dictionary that maps student names to a list of scores
grades = {}

# Use with statement to guarantee file closure
with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    first_row = True
    for row in grades_reader:
        # Skip the first row with column names
        if first_row:
            first_row = False
            continue

        ## Calculate final student grade ##

        name = row[0]

        # Convert score strings into floats
        scores = [float(cell) for cell in row[1:]]

        hw1_weighted = scores[0]/10 * 0.05
        hw2_weighted = scores[1]/10 * 0.05
        mid_weighted = scores[2]/100 * 0.40
        fin_weighted = scores[3]/100 * 0.50

        grades[name] = (hw1_weighted + hw2_weighted + 
                        mid_weighted + fin_weighted) * 100

for student, score in grades.items():
    print(f'{student} earned {score:.1f}%')
--------------------------------------------------------------

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        # Convert lines into dictionary
        shows_dict = {}
        for i in range(0, len(lines), 2):
            num_seasons = int(lines[i].strip())
            show = lines[i + 1].strip()
            if num_seasons in shows_dict:
                shows_dict[num_seasons].append(show)
            else:
                shows_dict[num_seasons] = [show]
        return shows_dict

def write_output_keys(output_file, shows_dict):
    with open(output_file, 'w') as file:
        sorted_keys = sorted(shows_dict.keys(), reverse=True)
        for key in sorted_keys:
            shows = '; '.join(shows_dict[key])
            file.write(f"{key}: {shows}\n")

def write_output_titles(output_file, shows_dict):
    with open(output_file, 'w') as file:
        all_shows = []
        for shows in shows_dict.values():
            all_shows.extend(shows)
        sorted_shows = sorted(all_shows, reverse=True)
        for show in sorted_shows:
            file.write(f"{show}\n")

def main():
    input_file = input("Enter the name of the input file: ")
    shows_dict = read_input_file(input_file)

    write_output_keys("output_keys.txt", shows_dict)
    write_output_titles("output_titles.txt", shows_dict)

if __name__ == "__main__":
    main()
    
-------------------------------------------------------------------------------