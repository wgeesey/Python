class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
      
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
    # TODO: Define print_info() method to output model_year, purchase_price, and current_value
    def print_info(self):
        print(
            f"Car's information:\n"
            f"  Model year: {self.model_year}\n"
            f"  Purchase price: ${self.purchase_price}\n"
            f"  Current value: ${self.current_value}"
            )

if __name__ == "__main__":    
    year = int(input()) 
    price = int(input())
    current_year = int(input())
    
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()
    
	


class FoodItem:
    # TODO: Define constructor with parameters to initialize instance 
    #       attributes (name, fat, carbs, protein)
    #Complete the FoodItem class by adding a constructor to initialize a food item. The constructor should 
    #initialize the name (a string) to "Water" and all other instance attributes to 0.0 by default. If the 
    #constructor is called with a food name, grams of fat, grams of carbohydrates, and grams of protein, the 
    #constructor should assign each instance attribute with the appropriate parameter value.
    #The given program accepts as input a food item name, amount of fat, carbs, and protein, and the number of 
    #servings. The program creates a food item using the constructor parameters' default values and a food item 
    #using the input values. The program outputs the nutritional information and calories per serving for a food 
    #item.
    
    def __init__(self, name="Water", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        
       
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories
       
    def print_info(self):
        print(f'Nutritional information per serving of {self.name}:')
        print(f'  Fat: {self.fat:.2f} g')
        print(f'  Carbohydrates: {self.carbs:.2f} g')
        print(f'  Protein: {self.protein:.2f} g')

if __name__ == "__main__":
       
    item_name = input()
    if item_name == 'Water' or item_name == 'water':
        food_item = FoodItem()
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')                       
    
    else:
        amount_fat = float(input())
        amount_carbs = float(input())
        amount_protein = float(input())
        num_servings = float(input())
        
        food_item = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
        food_item.print_info()
        print(f'Number of calories for {1.0:.2f} serving(s): {food_item.get_calories(1.0):.2f}')
        print(f'Number of calories for {num_servings:.2f} serving(s): {food_item.get_calories(num_servings):.2f}')
        
        


class Artist:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def __init__(self, name="unknown", birth=-1, death=-1):
        self.name = name
        self.birth_year = birth
        self.death_year = death
        
    def print_info(self):
        if (self.birth_year > 0) and (self.death_year > 0):
            print(f"Artist: {self.name} ({self.birth_year} to {self.death_year})")
        elif (self.birth_year > 0) and (self.death_year < 0):
            print(f"Artist: {self.name} ({self.birth_year} to present)")
        else:
            print(f"Artist: {self.name} (unknown)")


      
class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)
    def __init__(self, title="unknown", year_created=-1, artist=None):
        self.title = title
        self.year_created = year_created
        self.artist = artist
    # TODO: Define print_info() method
    def print_info(self):
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")

if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()




