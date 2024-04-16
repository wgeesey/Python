from collections import namedtuple

School = namedtuple('School', ['name', 'city', 'state', 'enrollment'])

school_data = School(input(), input(), input(), int(input()))

print("School name: " + school_data.name)
print("City: " + school_data.city)
print("State: " + school_data.state)
print("Enrollment: " + str(school_data.enrollment))







color_name = input()
red_channel = int(input())
green_channel = int(input())
blue_channel = int(input())

color_data = (color_name, red_channel, green_channel, blue_channel)

print(f'Color name: {color_data[0]}, R: {color_data[1]}, G: {color_data[2]}, B: {color_data[3]}')







from collections import namedtuple

Person = namedtuple('Person', ['first_name', 'last_name', 'birthday', 'license_plate'])

first_name = input()
last_name = input()
birthday = input()
license_plate = input()

person_info = Person(first_name, last_name, birthday, license_plate)

print(f'First name: {person_info.first_name}, Last name: {person_info.last_name}, Birthday: {person_info.birthday}, License plate: {person_info.license_plate}')







from collections import namedtuple

City = namedtuple('City', ['name', 'state', 'population'])

city_name = input()
state_located = input()
population_count = int(input())

city_info = City(city_name, state_located, population_count)

print(f'City name: {city_info.name}, State: {city_info.state}, Population: {city_info.population}')