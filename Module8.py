user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except ValueError:
        print('Could not calculate health info.\n')
    except ZeroDivisionError:
        print('Invalid height entered. Must be > 0.')

    user_input = input("Enter any key ('q' to quit): ")
    
    
-----------------------------------------------------------
# No exception handlers, not good approach
 
user_input = ''
while user_input != 'q':
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        print('Invalid weight.')
    else:
        height = int(input('Enter height (in inches): '))
        if height <= 0:
            print('Invalid height')
        
    if (weight < 0) or (height <= 0):
        print('Cannot compute info.')
    else:
        bmi = (float(weight) / float(height * height)) * 703
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
        
    user_input = input("Enter any key ('q' to quit): ")
    
-------------------------------------------------------------------
# Exception handlers and raise statements, better approach
user_input = ''
while user_input != 'q':
    try:
        weight = int(input('Enter weight (in pounds): '))
        if weight < 0:
            raise ValueError('Invalid weight.')

        height = int(input('Enter height (in inches): '))
        if height <= 0:
            raise ValueError('Invalid height.')

        bmi = (float(weight) * 703) / (float(height * height))
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")
------------------------------------------------------------------------
# Better with refactoring into get_height and get_weight functions

def get_weight():
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        raise ValueError('Invalid weight.')
    return weight

def get_height():
    height = int(input('Enter height (in inches): '))
    if height <= 0:
        raise ValueError('Invalid height.')
    return height

user_input = ''
while user_input != 'q':
    try:
        weight = get_weight()
        height = get_height()

        bmi = (float(weight) / float(height * height)) * 703
        print(f'BMI: {bmi}')
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")
-------------------------------------------------------------------
print('Opening file myfile.txt.')
f = open('myfile.txt')  # create file object

print('Reading file myfile.txt.')
contents = f.read()  # read file text into a string

print('Closing file myfile.txt.')
f.close()  # close the file

print('\nContents of myfile.txt:')
print(contents)

------------------------------------------------------------------
leek_file = open(input())

all_good = True
for line in leek_file:
    leeks = int(line)
    print(leeks)
    if leeks == 0:
        all_good = False

leek_file.close()

if all_good:
    print('All baskets have leeks.')
else:
    print('At least one basket is empty.')
---------------------------------------------------------
# Read file contents
print ('Reading in data....')
f = open('mydata.txt')
lines = f.readlines()
f.close()

# Iterate over each line
print('\nCalculating average....')
total = 0
for ln in lines:
    total += int(ln)

# Compute result
avg = total/len(lines)
print(f'Average value: {avg}')
-----------------------------------------------------------------
file_obj = open('expression.txt', 'w')
var1 = int(input())
var2 = int(input())

file_obj.write(str(var1))
file_obj.write(' * ')
file_obj.write(str(var2))
file_obj.write(' = ')
file_obj.write(str(var1 * var2) + '\n')


file_obj.close()

----------------------------------------------------------------

pigments_data = input()
new_pigment = input()

pigments_file = open(pigments_data, 'a+')
pigments_file.write(str(new_pigment))
pigments_file.flush()

# When a file is in update mode, 
# seek(0, 0) rewinds the file to enable reading from the beginning
pigments_file.seek(0, 0)  

file_data = pigments_file.read()
print(file_data)

pigments_file.close()

-------------------------------------------------------------
#os.path.split(path) – Splits a path into a two-tuple (head, tail), where tail is the last token in the path string
#and head is everything else.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print(os.path.split(p))
('C:\\Users\\BWayne', 'batsuit.jpg')

#os.path.exists(path) – Returns True if path exists, else returns False.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
if os.path.exists(p):
    print('Suit up....')
else:
    print('The Lamborghini then?')
If file exists:
Suit up....

If file does not exist:
The Lamborghini then?

#os.path.isfile(path) – Returns True if path is an existing file, and false otherwise (e.g., path is a directory).
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'bat_chopper')
if os.path.isfile(p):
    print('Found a file....')
else:
    print('Not a file....')
If path is a file:
Found a file....

If path is not a file:
Not a file....

#os.path.getsize(path) – Returns the size in bytes of path.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print(f'Size of file: {os.path.getsize(p)} bytes')
Size of file: 65544 bytes

-----------------------------------------------------------------------

import os

year = input('Enter year: ')
path = os.path.join('logs', year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)
Enter year:2009

logs\2009 contains subdirectories: ['April', 'January'] and the files: []
logs\2009\April contains subdirectories: ['1'] and the files: []
logs\2009\April\1 contains subdirectories: [] and the files: ['log.txt', 'words.doc']
logs\2009\January contains subdirectories: ['15', '21', '24'] and the files: []
logs\2009\January\15 contains subdirectories: [] and the files: ['log.txt']
logs\2009\January\21 contains subdirectories: [] and the files: ['log.txt', 'temp23.pdf']
logs\2009\January\24 contains subdirectories: [] and the files: ['presentation.ppt']

----------------------------------------------------------------------------------------------