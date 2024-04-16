 # Define your function here
def exact_change(user_total):
    if user_total <= 0:
        print('no change')
    
    # Calculate the number of quarters, dimes, nickels, and pennies
    num_quarters = user_total // 25
    user_total %= 25

    num_dimes = user_total // 10
    user_total %= 10

    num_nickels = user_total // 5
    user_total %= 5

    num_pennies = user_total
    
    change = (num_pennies, num_nickels, num_dimes, num_quarters)
    return change

if __name__ == '__main__': 
    input_val = int(input())    
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val) 
    change = [(num_pennies, 'penny'), (num_nickels, 'nickel'),
              (num_dimes, 'dime'), (num_quarters, 'quarter')]
    output = []
    for num_coins, coin_name in change:
        if num_coins > 1:
            if coin_name == 'penny':
                output.append((num_coins, 'pennies'))
            else:
                output.append((num_coins, coin_name + 's'))
        else:
            output.append((num_coins, coin_name))
    for coin in output:
        if coin[0] > 0:
            print(coin[0], coin[1])



# word = 'onomatopoeia'
# num_guesses = 10

# hidden_word = '-' * len(word)

# guess = 1

# while guess <= num_guesses and '-' in hidden_word:
    # print(hidden_word)
    # user_input = input(f'Enter a character (guess #{guess}): ')
    
    # if len(user_input) == 1:
        Count the number of times the character occurs in the word
        # num_occurrences = word.count(user_input)
    
        Replace the appropriate position(s) in hidden_word with the actual character.
        # position = -1
        # for occurrence in range(num_occurrences):
            # position = word.find(user_input, position+1)  # Find the position of the next occurrence
            # hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]  # Rebuild the hidden word string
    
        # guess += 1
        
# if not '-' in hidden_word:
    # print('Winner!', end=' ')        
# else:
    # print('Loser!', end=' ')

# print(f'The word was {word}.')


# menu_prompt = ('Available commands:\n'
               # '  (add) Add passenger\n'
               # '  (del) Delete passenger\n'
               # '  (print) Print passenger list\n'
               # '  (exit) Exit the program\n'
               # 'Enter command:\n')

# destinations = ['PHX', 'AUS', 'LAS'] 

# destination_prompt = ('Available destinations:\n'
                      # '(PHX) Phoenix\n'
                      # '(AUS) Austin\n'
                      # '(LAS) Las Vegas\n'
                      # 'Enter destination:\n')

# passengers = {}

# print('Welcome to Mohawk Airlines!\n')
# user_input = input(menu_prompt).strip().lower()

# while user_input != 'exit':
    # if user_input == 'add':
        # name = input('Enter passenger name:\n').strip().upper()
        # destination = input(destination_prompt).strip().upper()
        # if destination not in destinations:
            # print('Unknown destination.\n')
        # else:
            # passengers[name] = destination
            
    # elif user_input == 'del':
        # name = input('Enter passenger name:\n').strip().upper()
        # if name in passengers:
            # del passengers[name]

    # elif user_input == 'print':
        # for passenger in passengers:
            # print(f'{passenger.title()} --> {passengers[passenger]}')
    # else:
        # print('Unrecognized command.')

    # user_input = input('Enter command:\n').strip().lower()
  
  
  
 # name = input()

# tokens = name.split()

# lastName = tokens[-1]

# if len(tokens) == 3:
    # firstInitial = tokens[0][0]
    # middleInitial = tokens[1][0]
    # print(f"{lastName}, {firstInitial}.{middleInitial}.")
# else:
    # firstInitial = tokens[0][0]
    # print(f"{lastName}, {firstInitial}.")
    
# while True:
    # userInput = input()

    # tokens = userInput.split()

    # if tokens[0] == 'quit':
        # break

    # word = tokens[0]
    # number = int(tokens[1])

    # print(f'Eating {number} {word} a day keeps you happy and healthy.')
    
    
    
# inputString = input()

# result = ''

# for char in inputString:
    # if char.isalpha():
        # result += char
# print(result)

# OR

# inputString = input()

# result = ''

# for char in inputString:
    # if char.isalnum() and not char.isdigit():
        # result += char

# print(result)

#!/usr/bin/env python3
# pythonGlossary.py
# P. Brauda
# 2/1/20
# Glossary of Python terms using a dictionary

# # py_glossary = {
  # # "list" : "collection of items in a particular order",
  # # "dictionary" : "associative mapping of keys and values",
  # # "boolean expression" : "expression which evaluates to True or False",
  # # "for loop" : "iterative looping structure",
  # # "camel case" : "variable naming style using lower and upper case letters" 
# # }

# print the dictionary
# # print(py_glossary)

# print the keys only
# # print(sorted(py_glossary.keys()))

# print sorted keys and values separated by comma
# # for term in sorted(py_glossary):
    # # print(term, py_glossary[term], sep=',')

# delete "list" from dictionary
# # if "list" in py_glossary:
    # # del py_glossary["list"]

# print the dictionary again
# # print(py_glossary)