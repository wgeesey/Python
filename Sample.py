class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')
        print(f'   Annual: { self.is_annual }')
        print(f'   Color of flowers: { self.color_of_flowers }')

# TODO:  Define the print_list() function that prints a list of plant (or flower) objects 
def print_list(gardenList):
    for i, item in enumerate(gardenList, 1):
        print(f'Plant {i} Information:')
        item.print_info()
        print()    

if __name__ == "__main__":

    my_garden = []

    user_string = input()
    
    while user_string != '-1':
        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, is_annual, color_of_flowers
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        gardenInput = user_string.split()
        if gardenInput[0] == 'plant':
            plant_name, plant_cost = gardenInput[1], int(gardenInput[2])
            my_garden.append(Plant(plant_name, plant_cost))
        elif gardenInput[0] == 'flower': 
            plant_name, plant_cost, is_annual, color_of_flowers = gardenInput[1], int(gardenInput[2]), gardenInput[3], gardenInput[4]
            my_garden.append(Flower(plant_name, plant_cost, is_annual, color_of_flowers))
        
        user_string = input()
        

    # TODO: Call the print_list() function to print my_garden
    print_list(my_garden)