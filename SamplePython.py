size = 5

def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:', end=' ')
    for num in numbers:
        print(num, end=' ')
    print()

def print_odd_numbers(numbers):
    # Print all odd numbers
    odd_nums = [num for num in numbers if num % 2 != 0]
    print('Odd numbers:', end=' ')
    for num in odd_nums:
        print(num, end=' ')
    print()

def print_negative_numbers(numbers):
    # Print all negative numbers
    negative_nums = [num for num in numbers if num < 0]
    print('Negative numbers:', end=' ')
    for num in negative_nums:
        print(num, end=' ')
    print()

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)


----------------------------------------------------------------------------------------------------------

# def add_grade(student_grades):
    # print('Entering grade. \n')
    # name, grade = input(grade_prompt).split()
    # student_grades[name] = grade

# def delete_name(student_grades):
    # print('Deleting grade.\n')
    # name = input(delete_prompt)
    # del student_grades[name]
    
# def print_grades(student_grades):
    # print('Printing grades.\n')
    # for name, grade in student_grades.items():
        # print(f'{name} has a {grade}.')
    
# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
# delete_prompt = "Enter name to delete:\n"
# menu_prompt = ("1. Add/modify student grade\n"
                # "2. Delete student grade\n"
                # "3. Print student grades\n"
                # "4. Quit\n\n")

# command = input(menu_prompt).lower().strip()

# while command != '4':  # Exit when user enters '4'
    # if command == '1':
        # add_grade(student_grades)
    # elif command == '2':
        # delete_name(student_grades)  
    # elif command == '3':
       # print_grades(student_grades)   
    # else:
        # print('Unrecognized command.\n')

    # command = input().lower().strip()
    
    
----------------------------------------------------------------------------------------------   
    
    
# def multiply_nums(list_to_modify, num):
  # for i, element in enumerate(list_to_modify):
      # list_to_modify[i] = element * num
  # print(f'Modified list: {list_to_modify}')

# item_list = [int(x) for x in input().split()]
# number = int(input())

# multiply_nums(item_list[:], number)

# print(f'Original list: {item_list}')


-----------------------------------------------------------------------------------------------------------

# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

# def split_check(bill, people, tax_percentage=0.09, tip_percentage=0.15):
    # split = ((bill + bill*tip_percentage) + (bill * tax_percentage))/people
    # return split

# bill = float(input())
# people = int(input())

# # Cost per diner at the default tax and tip percentages
# print(f'Cost per diner: ${split_check(bill, people):.2f}')

# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())

# # Cost per diner at different tax and tip percentages
# print(f'Cost per diner: ${split_check(bill, people, new_tax_percentage, new_tip_percentage):.2f}')

-------------------------------------------------------------------------------------------------------------
# student_scores = [75, 84, 66, 99, 51, 65]

# def get_grade_stats(scores):
    # # Calculate the arithmetic mean
    # mean = sum(scores)/len(scores)
    
    # # Calculate the standard deviation
    # tmp = 0
    # for score in scores:
        # tmp += (score - mean )**2
    # std_dev = (tmp/len(scores))**0.5

    # # Package and return average, standard deviation in a tuple
    # return mean, std_dev

# # Unpack tuple
# average, standard_deviation = get_grade_stats(student_scores)

# print(f'Average score: {average}')
# print(f'Standard deviation: {standard_deviation}')

-------------------------------------------------------------------------------------------------------
# def num_seats(airliner_type):
    # """Determines number of seats on a plane"""
    # #Function body statements ...

# def ticket_price(origin, destination, coach=True, first_class=False):
    # """Calculates the price of a ticket between two airports.
    # Only one of coach or first_class must be True.

    # Arguments:
    # origin -- string representing code of origin airport
    # destination -- string representing code of destination airport

    # Optional keyword arguments:
    # coach -- Boolean. True if ticket cost priced for a coach class ticket (default True)
    # first_class -- Boolean. True if ticket cost priced for a first class ticket (default False)

    # """
    # #Function body statements ...
    
-------------------------------------------------------------------------------------------------    
# gas_constant = 8.3144621  # Joules / (mol*Kelvin)

# def convert_to_temp(pressure, volume, mols):
    # """Convert pressure, volume, and moles to a temperature"""
    # return (pressure * volume) / (mols * gas_constant)

# press = float(input('Enter pressure (in Pascals): '))
# vol = float(input('Enter volume (in cubic meters): '))
# mols = float(input('Enter number of moles: '))


# print(f'Temperature = {convert_to_temp(press, vol, mols):.2f} K')

--------------------------------------------------------------------------------------------------
# import math

# def trajectory(t, a, v, g, h): 
    # """Calculates new x,y position""" 
    # x = v * t * math.cos(a) 
    # y = h + v * t * math.sin(a) - 0.5 * g * t * t 
    # return (x,y)

# def degree_to_radians(degrees): 
    # """Converts degrees to radians""" 
    # return ((degrees * math.pi) / 180.0)

# gravity = 9.81 # Earth gravity (m/s^2) 
# time = 1.0 # time (s) 
# x_loc = 0 
# h = 0 

# angle = float(input('Launch angle (deg): ')) 
# print(angle) 
# angle = degree_to_radians(angle)

# velocity = float(input('Launch velocity (m/s): ')) 
# print(velocity)

# height = float(input('Initial height (m): '))  
# y_loc = height 
# print(y_loc)

# while ( y_loc >= 0.0 ): # While above ground 
    # print(f'Time {time:3.0f} x = {x_loc:3.0f} y = {y_loc:3.0f}')
    # x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)  
    # time += 1.0
 
-------------------------------------------------------------------------------------------------------- 
# def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    # cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
    # return cost

# if __name__ == '__main__':
    # miles_per_gallon = float(input())
    # dollars_per_gallon = float(input())
    # print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10):.2f}')
    # print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50):.2f}')
    # print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400):.2f}')
------------------------------------------------------------------------------------------------------------    
# def int_to_reverse_binary(integer_value):
    # string_to_reverse = ''
    # while integer_value > 0:
        # val = integer_value % 2
        # string_to_reverse += str(val)
        # integer_value //= 2
    # return string_to_reverse
    
# def string_reverse(input_string):
    # return input_string[::-1]

# if __name__ == '__main__':
    # # Type your code here. 
    # # Your code must call int_to_reverse_binary() to get 
    # # the binary string of an integer in a reverse order.
    # # Then call string_reverse() to reverse the string
    # # returned from int_to_reverse_binary().
    # integer_input = int(input())
    # input_binary = int_to_reverse_binary(integer_input)
    # print(f'{string_reverse(input_binary)}')

---------------------------------------------------------------------------------------------------        
# # Define your function here
# def exact_change(user_total):
    # if user_total <= 0:
        # print('no change')
    
    # # Calculate the number of quarters, dimes, nickels, and pennies
    # num_quarters = user_total // 25
    # user_total %= 25

    # num_dimes = user_total // 10
    # user_total %= 10

    # num_nickels = user_total // 5
    # user_total %= 5

    # num_pennies = user_total
    
    # change = (num_pennies, num_nickels, num_dimes, num_quarters)
    # return change
    

# if __name__ == '__main__': 
    # input_val = int(input())    
    # num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val) 
    # if num_pennies > 1:
        # print(num_pennies, 'pennies')
    # elif num_pennies == 1:
        # print(num_pennies, 'penny')
    # if num_nickels > 1:
        # print(num_nickels, 'nickels')
    # elif num_nickels == 1:
        # print(num_nickels, 'nickel')
    # if num_dimes > 1:
        # print(num_dimes, 'dimes')
    # elif num_dimes == 1:
        # print(num_dimes, 'dime')
    # if num_quarters > 1:
        # print(num_quarters, 'quarters')
    # elif num_quarters == 1:
        # print(num_quarters, 'quarter')    


---------------------------------------------------------------------------------------        
# # Define your function here
# def exact_change(user_total):
    # if user_total <= 0:
        # print('no change')
    
    # coins = [('quarter', 25), ('dime', 10), ('nickel', 5), ('penny', 1)]
    # change = []
    
    # for coin_name, coin_value in coins:
        # num_coins = user_total // coin_value
        # user_total %= coin_value
        
        # if num_coins > 1:
            # if coin_name == 'penny':
                # change.append((num_coins, 'pennies'))
            # else:
                # change.append((num_coins, coin_name + 's'))
        # else:
            # change.append((num_coins, coin_name))
            

    # return reversed(tuple(change))
    

# if __name__ == '__main__': 
    # input_val = int(input())    
    # num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val) 
    # for coin in (num_pennies, num_nickels, num_dimes, num_quarters):
        # if coin[0] > 0:
            # print(coin[0], coin[1])
            
------------------------------------------------------------------------------------------            
 # Define your function here
# def exact_change(user_total):
    # if user_total <= 0:
        # print('no change')
    
    # #Calculate the number of quarters, dimes, nickels, and pennies
    # num_quarters = user_total // 25
    # user_total %= 25

    # num_dimes = user_total // 10
    # user_total %= 10

    # num_nickels = user_total // 5
    # user_total %= 5

    # num_pennies = user_total
    
    # change = (num_pennies, num_nickels, num_dimes, num_quarters)
    # return change

# if __name__ == '__main__': 
    # input_val = int(input())    
    # num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val) 
    # change = [(num_pennies, 'penny'), (num_nickels, 'nickel'),
              # (num_dimes, 'dime'), (num_quarters, 'quarter')]
    # output = []
    # for num_coins, coin_name in change:
        # if num_coins > 1:
            # if coin_name == 'penny':
                # output.append((num_coins, 'pennies'))
            # else:
                # output.append((num_coins, coin_name + 's'))
        # else:
            # output.append((num_coins, coin_name))
    # for coin in output:
        # if coin[0] > 0:
            # print(coin[0], coin[1])
            
            


--------------------------------------------------------------------------------------------            
# plants = input().split()
# planted = input().split()
# separator_char = input()

# print(f'{"Plants":^39}|{"Planted":^39}')
# print(separator_char * 78)
# for i in range(0,3):
    # print(f'{plants[i]:^39}|{planted[i]:^39}')
    
-----------------------------------------------------------------------------------------------   
#!/usr/bin/env python3
# pythonGlossary.py
# P. Brauda
# 2/1/20
# Glossary of Python terms using a dictionary

# py_glossary = {
  # "list" : "collection of items in a particular order",
  # "dictionary" : "associative mapping of keys and values",
  # "boolean expression" : "expression which evaluates to True or False",
  # "for loop" : "iterative looping structure",
  # "camel case" : "variable naming style using lower and upper case letters" 
# }

# # print the dictionary
# print(py_glossary)

# # print the keys only
# print(sorted(py_glossary.keys()))

# # print sorted keys and values separated by comma
# for term in sorted(py_glossary):
    # print(term, py_glossary[term], sep=',')

# # delete "list" from dictionary
# if "list" in py_glossary:
    # del py_glossary["list"]

# # print the dictionary again
# print(py_glossary)



-----------------------------------------------------------------------------------------------
# def ordinal_suffix(num):
    # if 10 <= num % 100 <= 20:
        # suffix = "th"
    # else:
        # suffix = {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
    # return str(num) + suffix

# # Main program
# def main():
    # # List of known ages of the oldest people
    # oldest_ages = [122, 119, 117, 117, 116]

    # while True:
        # try:
            # # Ask the user for the nth oldest person
            # n = int(input("Enter the value of n (1-5): "))
            # if 1 <= n <= 5:
                # print(f"The age of the {ordinal_suffix(n)} oldest known person is {oldest_ages[n-1]}.")
                # break
            # else:
                # print("Please enter a number between 1 and 5.")
        # except ValueError:
            # print("Please enter a valid number.")

# if __name__ == "__main__":
    # main()

---------------------------------------------------------------------------------------------
# # Create dictionaries for each conference
# conferences = [
    # {
        # "ACC": {
            # "Clemson": "Tigers",
            # "Florida State": "Seminoles",
            # "Miami": "Hurricanes"
        # }
    # },
    # {
        # "SEC": {
            # "Alabama": "Crimson Tide",
            # "LSU": "Tigers",
            # "Georgia": "Bulldogs"
        # }
    # },
    # {
        # "Big Ten": {
            # "Ohio State": "Buckeyes",
            # "Michigan": "Wolverines",
            # "Penn State": "Nittany Lions"
        # }
    # }
# ]

# Accept user input to pick a conference
# print("Available Conferences:")
# for i, conference in enumerate(conferences, 1):
    # print(f"{i}. {list(conference.keys())[0]}")

# while True:
    # try:
        # conference_choice = int(input("Choose a conference (1-3): "))
        # if 1 <= conference_choice <= 3:
            # conference_index = conference_choice - 1
            # break
        # else:
            # print("Please enter a number between 1 and 3.")
    # except ValueError:
        # print("Please enter a valid number.")

# # Get the selected conference dictionary
# conference = conferences[conference_index][list(conferences[conference_index].keys())[0]]

# # Present the user with a list of teams to choose from
# print(f"Teams in the {list(conference.keys())[0]} conference:")
# for i, team in enumerate(conference.keys(), 1):
    # print(f"{i}. {team}")

# while True:
    # try:
        # team_choice = int(input("Choose a team: "))
        # if 1 <= team_choice <= len(conference):
            # team_index = team_choice - 1
            # break
        # else:
            # print("Please enter a valid team number.")
    # except ValueError:
        # print("Please enter a valid number.")

# # Display the team's mascot
# team = list(conference.keys())[team_index]
# mascot = conference[team]
# print(f"The mascot of {team} is {mascot}.")
------------------------------------------------------------------------------------------------------
# # Create dictionaries for each conference
# acc_dict = {"Clemson": "Tigers", "Florida State": "Seminoles", "Louisville": "Cardinals"}
# big_10_dict = {"Ohio State": "Buckeyes", "Michigan": "Wolverines", "Penn State": "Nittany Lions"}
# sec_dict = {"Alabama": "Crimson Tide", "Georgia": "Bulldogs", "LSU": "Tigers"}

# # Add dictionaries to a list
# conferences = [acc_dict, big_10_dict, sec_dict]

# # Accept user input for conference selection
# print("Choose a conference:")
# for i in range(len(conferences)):
    # print(f"{i+1}. {list(conferences[i].keys())[0]}")

# conf_num = int(input()) - 1

# # Check if the selected conference exists
# if 0 <= conf_num < len(conferences):
    # conference = conferences[conf_num]
    # teams = list(conference.keys())

    # # Accept user input for team selection
    # print("Choose a team:")
    # for i in range(len(teams)):
        # print(f"{i+1}. {teams[i]}")

    # team_num = int(input()) - 1

    # # Check if the selected team exists
    # if 0 <= team_num < len(teams):
        # team = teams[team_num]
        # mascot = conference[team]
        # print(f"The mascot for {team} is {mascot}.")
    # else:
        # print("Invalid team selection.")
# else:
    # print("Invalid conference selection.")
---------------------------------------------------------------------------------------------------------

# # Create dictionaries for each conference
# acc_dict = {"Clemson": "Tigers", "Florida State": "Seminoles", "Louisville": "Cardinals"}
# big_10_dict = {"Ohio State": "Buckeyes", "Michigan": "Wolverines", "Penn State": "Nittany Lions"}
# sec_dict = {"Alabama": "Crimson Tide", "Georgia": "Bulldogs", "LSU": "Tigers"}

# # Add dictionaries to a list
# conferences = [acc_dict, big_10_dict, sec_dict]

# # Accept user input for conference selection
# print("Choose a conference:")
# for i, conf in enumerate(conferences):
    # print(f"{i+1}. {list(conf.keys())[0]}")

# conf_num = int(input()) - 1

# # Check if the selected conference exists
# if conf_num >= 0 and conf_num < len(conferences):
    # conference = conferences[conf_num]
    # teams = list(conference.keys())

    # # Accept user input for team selection
    # print("Choose a team:")
    # for i, team in enumerate(teams):
        # print(f"{i+1}. {team}")

    # team_num = int(input()) - 1

    # # Check if the selected team exists
    # if team_num >= 0 and team_num < len(teams):
        # team = teams[team_num]
        # mascot = conference[team]
        # print(f"The mascot for {team} is {mascot}.")
    # else:
        # print("Invalid team selection.")
# else:
    # print("Invalid conference selection.")
    
---------------------------------------------------------------------------------    
    
# riders_per_ride = 3  # Num riders per ride to dispatch

# line = []  # The line of riders
# num_vips = 0  # Track number of VIPs at front of line

# menu = ('(1) Reserve place in line.\n'  # Add rider to line
        # '(2) Reserve place in VIP line.\n'  # Add VIP
        # '(3) Dispatch riders.\n'  # Dispatch next ride car
        # '(4) Print riders.\n'
        # '(5) Find position in line.\n'
        # '(6) Remove from line.\n'
        # '(7) Exit.\n\n')

# user_input = input(menu).strip().lower()

# while user_input != '7':
    # if user_input == '1':  # Add rider
        # name = input('Enter name:').strip().lower()
        # line.append(name)

    # elif user_input == '2':  # Add VIP
        # name = input('Enter name:').strip().lower()
        # line.insert(num_vips, name)
        # num_vips += 1

    # elif user_input == '3':  # Dispatch ride
        # if line:
            # for _ in range(riders_per_ride):
                # if line:
                    # line.pop(0)
                    # if num_vips > 0:
                        # num_vips -= 1

    # elif user_input == '4':  # Print riders waiting in line
        # print(f'{len(line)} person(s) waiting: {line}')

    # elif user_input == '5':  # Find position in line
        # name = input('Enter name to find position: ').strip().lower()
        # if name in line:
            # position = line.index(name) + 1
            # print(f'{name} is in position {position} in line.')
        # else:
            # print(f'{name} is not in line.')

    # elif user_input == '6':  # Remove from line
        # name = input('Enter name to remove: ').strip().lower()
        # if name in line:
            # line.remove(name)
            # if line.index(name) < num_vips:
                # num_vips -= 1
        # else:
            # print(f'{name} is not in line.')

    # else:
        # print('Unknown menu option')

    # user_input = input('Enter command: ').strip().lower()

---------------------------------------------------------------------------------

# user_input = input('Enter numbers:')

# tokens = user_input.split()  # Split into separate strings

# # Convert strings to integers
# nums = []
# for token in tokens:
    # nums.append(int(token))

# # Print each position and number
# print()  # Print a single newline
# for index in range(len(nums)):
    # value = nums[index]
    
    # print(f'{index}: {value}')

# # Determine maximum even number
# max_num = None
# for num in nums:
    # if (max_num == None) and (num % 2 == 0):
        # # First even number found
        # max_num = num
    # elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
        # # Larger even number found
        # max_num = num

# print(f'Max even #: {max_num}')

---------------------------------------------------------------------------------------


# # User inputs string w/ numbers: '203 12 5 800 -10'
# user_input = input('Enter numbers: ')

# tokens = user_input.split()  # Split into separate strings

# # Convert strings to integers
# print()
# nums = []
# for pos, token in enumerate(tokens):
    # nums.append(int(token))
    # print(f'{pos}: {token}')

# # Calculate sum and average
# sum_nums = sum(nums)
# average = sum_nums / len(nums)

# print(f'Sum: {sum_nums}')
# print(f'Average: {average}')

# # Print numbers greater than 21
# print('Numbers greater than 21:')
# for num in nums:
    # if num > 21:
        # print(num)





---------------------------------------------------------------------------------------------

# #Lebron James: Statistics for 2003/2004 - 2012/2013
# games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
# points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
# assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
# rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# # Print total points
# print(f'Total Career Points: {sum(points)}')

# # Print Average PPG
# print(f'Average Points Per Game: {(sum(points) / sum(games_played)):.2f}')

# # Print best scoring years (Ex: 2004/2005)
## maxScore = max(points)
# maxIndex = points.index(max(points))
# print(f'Highest Scoring Season: {2003 + maxIndex} / {2004 + maxIndex}') 
# Print worst scoring years (Ex: 2004/2005)
# #minScore = min(points)
# minIndex = points.index(min(points))
# print(f'Lowest Scoring Season: {2003 + minIndex} / {2004 + minIndex}') 

--------------------------------------------------------------------------------------------------

# user_input = input()
# test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


# sum_extra = 0 # Initialize 0 before your loop

# for grade in test_grades:
    # if grade > 100:
        # sum_extra += grade - 100

# print(f'Sum extra: {sum_extra}')

---------------------------------------------------------------------------------------

# # Read input and split input into tokens
# tokens = input().split()

# measurements_list = []
# for token in tokens:
    # measurements_list.append(int(token))

# print(f'Raw samples: {measurements_list}')

# num_ok = 0

# for value in measurements_list:
    # if value < 50:
        # print(f'{value} at index {measurements_list.index(value)} needs attention')
    # else:
        # num_ok += 1
        # print(f'{value} at index {measurements_list.index(value)} is ok')

# print(f'Total ok samples: {num_ok}')



---------------------------------------------------------------------------------------


# # Read input and split input into tokens
# tokens = input().split()

# measurements_list = []
# for token in tokens:
    # measurements_list.append(int(token))

# print(f'Raw samples: {measurements_list}')

# num_ok = 0

# for index, value in enumerate(measurements_list):
    # if value < 50:
        # print(f'{value} at index {index} needs attention')
    # else:
        # num_ok += 1
        # print(f'{value} at index {index} is ok')

# print(f'Total ok samples: {num_ok}')



---------------------------------------------------------------------------------------------


# # Read input and split input into tokens
# tokens = input().split()

# measurements_list = []
# for token in tokens:
    # measurements_list.append(int(token))

# print(f'All data: {measurements_list}')

# sum_good = 0
# for index, value in enumerate(measurements_list):
    # if index % 2 != 0 and value < 60:
        # print(f'Index {index}: {value}')
        # sum_good += value
        

# print(f'Sum of selected elements is: {sum_good}')



------------------------------------------------------------------------------------------

# # Read input and split input into tokens
# tokens = input().split()

# input_list = []
# for token in tokens:
    # input_list.append(int(token))

# print(f'Sequence: {input_list}')

# max_diff = None

# for i in range(1, len(input_list)):
    # neighbor_diff = input_list[i] - input_list[i-1]
    # print(f'{input_list[i]} - {input_list[i-1]} = {neighbor_diff}')
    # if max_diff is None or neighbor_diff > max_diff:
        # max_diff = neighbor_diff
    

# print(f'The largest difference between two neighboring values is {max_diff}')




--------------------------------------------------------------------------------------------------


# currency = [
   # [1, 5, 10 ],  # US Dollars
   # [0.75, 3.77, 7.53],  #Euros
   # [0.65, 3.25, 6.50]  # British pounds
# ]
# for row_index, row in enumerate(currency):
   # for column_index, item in enumerate(row):
       # print(f'currency[{row_index}][{column_index}] is {item:.2f}')
       
       
       
# currency = [

        # [1.00, 5.00, 10.0], # US Dollars
        # [0.75, 3.77, 7.53], # Euros
        # [0.65, 3.25, 6.50]  # British pounds
# ]

# for row in currency:
    # for cell in row:
        # print(cell, end=' ')
    # print()

-------------------------------------------------------------------------------------------------


# # Read the tic-tac-toe board from input
# ttt_board = [
  # input().split(),
  # input().split(),
  # input().split()
# ]

# # Check if all elements at column index 1 are 'x'
# column_1_elements = [row[1] for row in ttt_board]
# if all(element == 'x' for element in column_1_elements):
    # print('Column 1 wins.')
# else:
    # print('No win at column 1.')
    
----------------------------------------------------------------------------------------------
# ttt_board = [
  # input().split(),
  # input().split(),
  # input().split()
# ]

# if (ttt_board[0][1] == 'x' and ttt_board[1][1] == 'x' and ttt_board[2][1] == 'x'):
    # print('Column 1 wins.')
# else:
    # print('No win at column 1.') 


# num_salads = int(input())
# salad_ingredients = []
# for row_index in range(num_salads):
    # salad_ingredients.append(input().split())

# for row_index, row in enumerate(salad_ingredients):
    # print(f'Fruit salad {row_index + 1}:')
    # for column_index, ingredient in enumerate(row):
        # print(salad_ingredients[row_index][column_index], end = ' ')
    # print()
    


---------------------------------------------------------------------------

# grid_size = int(input())

# pattern_2d = []
# for j in range(grid_size):
    # row = []
    # for k in range(grid_size):
        # row.append(0)
    # pattern_2d.append(row)

# #for j in range(grid_size):
# #    for k in range(grid_size):
# #        pattern_2d[j][k] = j + k - 3

# for j, row in enumerate(pattern_2d):
    # for k, value in enumerate(row):
        # pattern_2d[j][k] = j + k - 3

# for row in pattern_2d:
    # for cell in row:
        # print(cell, end=' ')
    # print()
    
--------------------------------------------------------------------    

# april_data = []
# for token in input().split():
	# april_data.append(int(token))

# slice_size = len(april_data)//3
# early_april = april_data[:slice_size]
# mid_april = april_data[slice_size:(2*slice_size)]
# late_april = april_data[2*slice_size:]

# print(f'Number of data in each third: {slice_size}')
# print(f'April data: {april_data}')
# print(f'Early April: {early_april}')
# print(f'Mid April: {mid_april}')
# print(f'Late April: {late_april}')

-----------------------------------------------------------------------------------------

# data_list = []
# for token in input().split():
	# data_list.append(int(token))

# backup_data = data_list[:]
# samples_picked = data_list[0::3]

# data_list.clear()
# print(f'Backup data list: {backup_data}')
# print(f'Samples selected: {samples_picked}')


------------------------------------------------------------------------------------------
#Changes elements of the list using a loop

my_list = [3.2, 5.0, 16.5, 12.25]

for i in range(len(my_list)):
    my_list[ i ] += 5
    
---------------------------------------------------------------------------

#Correct way to modify the list. TO edit the values, need to reference the index of the value.
user_input = input('Enter numbers: ')

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()
for pos, val in enumerate(nums):  
    
    print(f'{pos}: {val}')

# Change negative values to 0
for pos in range(len(nums)):
    if nums[pos] < 0:
        nums[pos] = 0

# Print new numbers
print('New numbers: ')
for num in nums:
    print(num, end=' ')
    

#Incorrect way: list not modified.
user_input = input('Enter numbers:')

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()
for pos, val in enumerate(nums):  
    
    print(f'{pos}: {val}')

# Change negative values to 0
for num in nums:
    if num < 0:
        num = 0  # Logic error: temp variable num set to 0

# Print new numbers
print('New numbers: ')
for num in nums:
    print(num, end=' ')
    
--------------------------------------------------------------------------------------------

user_values = [1, 6, 7, 4]

max_value = user_values[0]
for pos in range(len(user_values)):
  if user_values[pos] >= max_value:
    max_value = user_values[pos]
    print(max_value)
    
---------------------------------------------------------------------------------------------

nums = [10, 20, 30, 40, 50]

for pos in range(len(nums)):
    tmp = nums[pos] / 2
    if (tmp % 2) == 0:
        nums[pos] = tmp

--------------------------------------------------------------------------------------------------

nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums2.append(int(val))

# Create a copy of nums1 to iterate over
nums1_copy = nums1.copy()

# Remove elements from nums1 if also in nums2
for val in nums1[:]:
    if val in nums2:
        print(f'Deleting {val}')
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')


-----------------------------------------------------------------------------------------------

nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums2.append(int(val))

# Create a new list containing only elements from nums1 that are not in nums2
nums1_new = [num for num in nums1 if num not in nums2]

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1_new:
    print(num, end=' ')


-----------------------------------------------------------------------------------------------------

chopsticks_list = []

tokens = input().split()
for token in tokens:
    chopsticks_list.append(int(token))
  
print('Original chopsticks:', end=' ')
for table in chopsticks_list:
    print(table, end=' ')
print()

for i in range(len(chopsticks_list)):
    if chopsticks_list[i] % 2 == 1:  
        chopsticks_list[i] += 1


print('Corrected chopsticks:', end=' ')
for table in chopsticks_list:
    print(table, end=' ')
print()

----------------------------------------------------------------------------------

food_available = input().split()
allergies_list = input().split()
  
print('Food on menu:', end=' ')
for food in food_available:
    print(food, end=' ')
print()

print('Food to avoid:', end=' ')
for food in allergies_list:
    print(food, end=' ')
print()

for food in food_available[:]:
    if food in allergies_list:
        print(f'{food} not picked')
        food_available.remove(food)

print('Safe to eat:', end=' ')
for food in food_available:
    print(food, end=' ')
print()

----------------------------------------------------------------------------------------

#Add 10 to every element.	
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[ i ] += 10
print(my_list)

my_list = [5, 20, 50]
my_list = [(i+10) for i in my_list]
print(my_list)

#Convert every element to a string.	
my_list = [5, 20, 50]
for i in range(len(my_list)):
    my_list[ i ] = str(my_list[ i ])
print(my_list)
my_list = [5, 20, 50]
my_list = [str(i) for i in my_list]
print(my_list)


#Convert user input to a list of integers.	
inp = input('Enter numbers:')
my_list = []
for i in inp.split():
    my_list.append(int(i))
print(my_list)
inp = input('Enter numbers:')
my_list = [int(i) for i in inp.split()]
print(my_list)

#Find the sum of each row in a two-dimensional list.	
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
print(sum_list)
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = [sum(row) for row in my_list]
print(sum_list)

#Find the sum of the row with the smallest sum in a two-dimensional table.	
my_list = [[5, 10, 15], [2, 3, 16], [100]]
sum_list = []
for row in my_list:
    sum_list.append(sum(row))
min_row = min(sum_list)
print(min_row)
my_list = [[5, 10, 15], [2, 3, 16], [100]]
min_row = min([sum(row) for row in my_list])
print(min_row)

-------------------------------------------------------------------------------------------------

input_list = []

# Read input
tokens = input().split()
for token in tokens:
    input_list.append(int(token))

computed_list = [element * 3 for element in input_list]

print(f'Original: {input_list}')
print(f'Computed: {computed_list}')


-----------------------------------------------------------------------------------------------

# Read input
multiples_list = [int(x) for x in input().split()]

filtered_list = [num for num in multiples_list if (num % 4 == 0)]

print(f'All numbers: {multiples_list}')
print(f'Multiples of 4: {filtered_list}')

-----------------------------------------------------------------------------------

import sys

if len(sys.argv) != 3:
    print('Usage: python myprog.py name age\n')
    sys.exit(1)  # Exit the program, indicating an error with 1.

name = sys.argv[1]
age = int(sys.argv[2])

print(f'Hello {name}. ')
print(f'{age} is a great age.\n')

-----------------------------------------------------------------------------------


student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
del_prompt = "Enter a name to delete:"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        student_grades[name] = grade
    elif command == '2':
        name = input(del_prompt)
        del student_grades[name]
    elif command == '3':
        print(student_grades)
    elif command == '4':
        break
    else:
        print('Unrecognized command.')
    print()

---------------------------------------------------------------------------------------

orders_record = {}
num_data = int(input())

for item in range(num_data):
    userInput = input().split()
    orders_record[userInput[0]] = userInput[1]

print('Orders record:')
print(orders_record)

OR 

orders_record = {}
num_data = int(input())

for item in range(num_data):
    key, value = input().split()
    orders_record[key] = value

print('Orders record:')
print(orders_record)

---------------------------------------------------------------------------------

favorite_food = {'Mai': 'lemon', 'Fay': 'grape'}

userInput = input()

while userInput.lower() != 'end':
    if userInput in favorite_food:
        del favorite_food[userInput]
    else:
        print(userInput, 'not a key')
    userInput = input()

print('Updated favorite food:')
print(favorite_food)

----------------------------------------------------------------------------------

my_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)

my_dict.update(dict(soda=1.49, burger=3.69))
burger_price = my_dict.get('burger', 0)
print(burger_price)

-----------------------------------------------------------------------------------

contact_dict1 = {'Rob': 'usr1@chocolate1.com'}
contact_dict2 = {}
ref_record1 = contact_dict1  # For testing purposes, ref_record1 references contact_dict1
ref_record2 = contact_dict2  # For testing purposes, ref_record2 references contact_dict2

input_line = input()
while input_line != 'exit':
	name, email = input_line.split()
	contact_dict2[name] = email
	input_line = input()

contact_dict1.clear()
contact_dict1.update(contact_dict2)

print('Contact dictionary 1:')
print(contact_dict1)
print('Contact dictionary 2:')
print(contact_dict2)


-------------------------------------------------------------------------------------------

resident_mailboxes = {'Kai': 'B675', 'Ava': 'B511', 'Eve': 'F810', 'Mai': 'G811'}
unread_mail = {'B675': 14, 'B511': 8, 'F810': 18, 'G811': 18}

resident_name = input()

mailbox_code = resident_mailboxes.get(resident_name, 'unavailable')
num_mail = unread_mail.pop(mailbox_code, -99)


print(f'{resident_name} (mailbox {mailbox_code}) picked up {num_mail} letters.')
print('Remaining mail:')
print(unread_mail)

-------------------------------------------------------------------------------------------------

solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

sorted_distance_list = sorted(list_of_distances)
closest = sorted_distance_list[0]
next_closest = sorted_distance_list[1]

print(f'Closest planet is {closest:.4e}')
print(f'Second closest planet is {next_closest:.4e}')

---------------------------------------------------------------------------------------------------

# Calculate total points for each student
total_points = {name: sum(scores) for name, scores in student_grades.items()}

# Find the student with the highest total points
best_student = max(total_points, key=total_points.get)
best_student_total_points = total_points[best_student]

# Calculate grade percentage for each student
grade_percentages = {name: (sum(scores) / len(scores)) for name, scores in student_grades.items()}

# Find the average score of each assignment
num_students = len(student_grades)
average_scores = [sum(scores) / num_students for scores in zip(*student_grades.values())]

# Find the curve to apply
curve = 100 / best_student_total_points

# Apply curve to each student's total score
curved_grades = {name: [score * curve for score in scores] for name, scores in student_grades.items()}

print("Name and grade percentage of the best student:")
print(f"{best_student}: {grade_percentages[best_student]}%")

print("\nAverage score of each assignment:")
for i, score in enumerate(average_scores):
    print(f"Assignment {i+1}: {score}")

print("\nCurved grades for each student:")
for name, scores in curved_grades.items():
    print(f"{name}: {scores}")
    
----------------------------------------------------------------------------------------------------
# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}
#create empty dict for assignment avgs
grade_per_assgn_avg = {   
    }
#Print the name and grade percentage of the 
#student with the highest total of points.
highest_total_points = 0
name = ''
grade = 0.00
for key,grades in student_grades.items():
   total_points = sum([num for num in grades])
   if highest_total_points < total_points:
      highest_total_points = total_points
      name = key
      grade = (highest_total_points/len(grades))  
print ('Student: {}, Grade: {}%\n'.format(name, grade))

#print assignment averages that were added to
#a new dict
i=0
while i< len(grades):
    assgn_total=0
    for grades in student_grades.values():
        assgn_total += grades[i]
        grade_per_assgn_avg[i+1] = assgn_total/len(student_grades.keys())
    i += 1
print('Average Grade Per Assignment: \n',grade_per_assgn_avg,'\n')

#add curve using grade var calc highest points above
percent_diff = 100-grade
last_grade = 0
save_name = ''
print('With Curve:')
for student,grades in student_grades.items():
    total_per_st = sum(student_grades[student])
    if total_per_st > last_grade:
        save_name = student
        percentage = ((sum(student_grades[save_name]))/len(grades)) + percent_diff
        print(save_name, percentage, '%')
        
        

# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

highest_total_points = 0

gradePerAssign = {}
for student, grades in student_grades.items():
    print(student, grades)
    total = sum(grades)
    print(total)
    if total > highest_total_points:
        highest_total_points = total
        name = student
        grade = (highest_total_points/len(grades))
print(f'Student: {name} Grade: {grade}') 

numStudents = len(student_grades)

for i in range(numStudents):
    assignmentScores = 0
    for grades in student_grades.values():
        assignmentScores += grades[i]
    gradePerAssign[i + 1] = assignmentScores / numStudents
    print(gradePerAssign[i + 1])
print(f'Averages: {gradePerAssign}')

print(f'{"Student":8} {"Grades":6} {"Curved-Grades":12}')
curve = 100 - grade
for student, grades in student_grades.items():
    studentTotal = sum(grades)
    normGrades = (studentTotal / len(grades))
    curvedScore = normGrades + curve
    print(f'{student:<8} {normGrades:^6.1f} {curvedScore:^12.1f}')

------------------------------------------------------------------------------------

Multiple key-value pairs, each representing a person's name and favorite/ordered food, 
are read from input and added to favorite_food. 
Assign sorted_keys with a sorted list of the keys in favorite_food.    
   
favorite_food = {}

input_line = input()
while input_line != 'quit':
    name, food = input_line.split()
    favorite_food[name] = food
    input_line = input()

sorted_keys = sorted(favorite_food)

print(sorted_keys)

----------------------------------------------------------------------------------------------

Multiple key-value pairs, each representing a person's name and favorite/ordered food, 
are read from input and added to favorite_food. 
In sorted order of the keys, output each key-value pair on one line, as follows:

favorite_food = {}

input_line = input()
while input_line != 'exit':
    name, food = input_line.split()
    favorite_food[name] = food
    input_line = input()


for key, value in sorted(favorite_food.items()):
    print(f'Name: {key}, Food: {value}')


----------------------------------------------------------------------------------------------------

from statistics import mean

numbers = []

numberInput = input().split()

for number in numberInput:
    numbers.append(float(number))
    
numbersMax = max(numbers)
numbersAverage = mean(numbers)
    
print(f'{numbersMax:.2f} {numbersAverage:.2f}')

------------------------------------------------------------------------------------------------

numberInput = input().split()
start, stop = input().split()

start = int(start)
stop = int(stop)

for num in numberInput:
    num = int(num)
    if start <= num <= stop:
        print(num, end = ",")
        
-------------------------------------------------------------------------------------------

# Get the list of name-phone number pairs
contacts_input = input().split()

# Create an empty dictionary to store contacts
contacts = {}

# Iterate over the list in steps of 2 to get pairs of name and phone number
for i in range(0, len(contacts_input), 2):
    name = contacts_input[i]
    phone_number = contacts_input[i + 1]
    contacts[name] = phone_number

# Get the name to search for
search_name = input()

# Output the phone number associated with the search name
print(contacts[search_name])


----------------------------------------------------------------------------

contacts = {}

contactInput = input().split()
searchName = input()

for info in contactInput:
    name, number = info.split(',')
    contacts[name] = number
    
    
if searchName in contacts:
    print(contacts[searchName])
    
    
----------------------------------------------------------------------------------------

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input().capitalize()
service_choice2 = input().capitalize()

#A '-' signifies an additional service was not selected. 
#Output all selected services, according to the input order, 
#along with the corresponding costs and then the total price for all car wash services.

print("ZyCar Wash")
print(f"Base car wash - ${base_wash}")

if service_choice1 != '-':
    total += services.get(service_choice1, 0)
    print(f"{service_choice1} - ${services.get(service_choice1, 0)}")

if service_choice2 != '-':
    total += services.get(service_choice2, 0)
    print(f"{service_choice2} - ${services.get(service_choice2, 0)}")

print("-----")
print(f"Total price: ${base_wash + total}")

---------------------------------------------------------------------------------------------

# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer 
    # indicating that word's frequency.
    freq_dict = {}
    for word in words:
        freq_dict[word] = words.count(word)
    return freq_dict

# The following code asks for input, splits the input into a word list, 
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(f'{ key } - { str(your_dictionary[key]) }')
        
--------------------------------------------------------------------------------------------

def in_order(nums):
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            return False
    return True
    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In descending order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [10, 8, 7, 6, 5]
    if in_order(nums2):
        print('In descending order')
    else:
        print('Not in order')
        
--------------------------------------------------------------------------------------
def get_max_int(nums):
    maxValue = max(nums)
    return maxValue
    
if __name__ == '__main__':

    inputVal = int(input())

    inputList = []

    while inputVal != -1:
        inputList.append(inputVal)
        inputVal = int(input())

    maxVal = get_max_int(inputList)

    for num in inputList:
        newVal = maxVal - num
        print(newVal)
        
----------------------------------------------------------------------------------------


user_values = []   # List of integers from input
userInput = input().split()
for num in userInput:
    num = int(num)
    user_values.append(num)

if len(user_values) > 2:
    user_values.append(user_values.pop(0))
    user_values.insert(0, user_values.pop(-2))
else:
    user_values.append(user_values.pop(0))


#print(*(str(num) for num in user_values), sep=" ")
#print(" ".join(map(str, user_values)))

for num in user_values:
    print(num, end = ' ')
print()
