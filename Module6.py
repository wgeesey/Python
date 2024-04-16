#!/usr/bin/env python3

#Module6.py
#P.Brauda
#2/19/2020
#Code from the slides

# greeter.py
#!/usr/bin/env python3

##def greet_user(name):   # (name) is the function parameter
##    """Display a simple greeting"""
##    print("Hello,", name, end="!")
##
##greet_user("Gina")   #"Gina" is the argument
##
### name = "Gina", like an assignment statement


##def describe_pet(animal_type, pet_name):
##       """Display information about a pet.""" ##docstring
##       print(f"\nI have a {animal_type}.")
##       print(f"My {animal_type}'s name is {pet_name.title()}.")
##
##describe_pet('hamster', 'harry') #function call with positional arguments
###describe_pet('harry', 'hamster')
##
###animal_type = 'hamster'
###pet_name = 'harry'
##
###print("printing the docstring: ")
###print (describe_pet.__doc__)
##
##describe_pet(animal_type='hamster', pet_name='harry')#keyword arguments 
##describe_pet(pet_name='fluffy',animal_type='cat')#keyword args not in positional order

##def describe_pet(pet_name, animal_type='dog'):
##    """Display information about a pet.
##
##       dog is the default animal_type."""
##    
##    print(f"\nI have a {animal_type}.")
##    print(f"My {animal_type}'s name is {pet_name.title()}.")
##
##describe_pet(pet_name='willie')   # no animal_type
##describe_pet(pet_name='fluffy', animal_type='cat')
##describe_pet('Tweety', 'bird')
##
##def get_formatted_name(first_name, last_name):
##    """Return a full name, neatly formatted."""
##    full_name = f"{first_name} {last_name}"
##    return full_name.title()
##
##musician = get_formatted_name('jimi', 'hendrix')
##print(musician)
##
#musician = full_name.title()

##def get_formatted_name(first_name, last_name, middle_name=''):
##     """Return a full name, neatly formatted."""
##     if middle_name: #if not empty because it has a value
##           full_name = f"{first_name} {middle_name} {last_name}"
##     else:
##           full_name = f"{first_name} {last_name}"
##     return full_name.title()
##
##musician = get_formatted_name('jimi', 'hendrix')
##print(musician)
##musician = get_formatted_name('john', 'hooker', 'lee')
##print(musician)
##
##def build_person(first_name, last_name):
##    """Return a dictionary of information about a person."""
##    person = {'first': first_name, 'last': last_name}
##    return person
##
##musician = build_person('jimi', 'hendrix')
####print(musician)  #this time printing a dictionary
####
##
##def greet_users(names):
##    """Print a simple greeting to each user in the list."""
##    for name in names:
##        msg = f"Hello, {name.title()}!"
##        print(msg)
##
##usernames = ['hannah', 'ty', 'margot']
##greet_users(usernames)
##
###names = usernames
##
###initial lists
##unprinted_designs = ['toy cannon', 'dragon', 'python', 'hulk']
##completed_models =[]
##
### manage lists of 3D printer models
##def print_models(unprinted_designs, completed_models):
##       """
##       Simulate printing each design, until none are left.
##       Move each design to completed_models after printing.
##       """
##       while unprinted_designs:
##           current_design = unprinted_designs.pop(0)
##           print(f"Printing model: {current_design}")
##           completed_models.append(current_design)
###pop() removes from the end of the list
###pop(0) removes from the beginning of the list
##           
##def show_completed_models(completed_models):
##       """Show all the models that were printed."""
##       print("\nThe following models have been printed:")
##       for completed_model in completed_models:
##           print(completed_model)
##
###passing lists to functions
####show_completed_models(completed_models)
####print_models(unprinted_designs, completed_models)
####show_completed_models(completed_models)#the modified list
####print(f"The unprinted_designs list is empty: {unprinted_designs}")
##
##unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
##completed_models = []
##
##print_models(unprinted_designs, completed_models)
##show_completed_models(completed_models)


#don't allow unprinted_designs to be modified
### manage lists of 3D printer models
##def print_models(unprinted_designs, completed_models):
##       """
##       Simulate printing each design, until none are left.
##       Move each design to completed_models after printing.
##       """
##       while unprinted_designs:
##           current_design = unprinted_designs.pop(0)
##           print(f"Printing model: {current_design}")
##           completed_models.append(current_design)
##
##def show_completed_models(completed_models):
##       """Show all the models that were printed."""
##       print("\nThe following models have been printed:")
##       for completed_model in completed_models:
##           print(completed_model)
##
##unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
##completed_models = []
##
##print_models(unprinted_designs[:], completed_models)
##show_completed_models(completed_models)
##print(f"The unprinted_designs list is unchanged: {unprinted_designs}")


#passing an arbitrary number of arguments
###use the * in front of the parameter to create an empty tuple
##def make_pizza(*toppings):
##    print(toppings)
##
##make_pizza("pepperoni")
##make_pizza("pepperoni", "mushrooms", "extra cheese")


#mixing positional and arbitrary arguments
##def make_pizza(size, *toppings):
##    print(f"\nMaking a {size}-inch pizza with these toppings: ")
##    for topping in toppings:
##        print(f"- {topping}")
##
##make_pizza(12, "pepperoni")
##make_pizza(18, "pepperoni", "mushrooms", "extra cheese")

###using a top-level scope check
##import temperature as temp
##def main():
##    print(f"55 fahrenheit is {temp.to_celsius(55)} celsius")
##
##if __name__ == "__main__":
##     main()

##x = lambda a: a + 10
##print(f"Using a simple lambda function: {x(5)}")
##
##x = lambda a, b, c : a + b + c
##print(f"Using a simple lambda function again: {x(5, 6, 2)}")




