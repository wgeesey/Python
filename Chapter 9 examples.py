class Length:
    def __init__(self):
        self.start_val = 0
        self.end_val = 0

    def compute_length(self):
        return self.end_val - self.start_val
        
len1 = Length()
len1.start_val = int(input())
len1.end_val = int(input())

len2 = Length()
len2.start_val = int(input())
len2.end_val = int(input())

print(f'First length: {len1.compute_length()}')
print(f'Second length: {len2.compute_length()}')



class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def print_length_width(self, string1):
        print(f'{string1}Length: {self.length}, width: {self.width}') 

rectangle1 = Rectangle()
rectangle1.length = int(input())
rectangle1.width = int(input())

rectangle2 = Rectangle()
rectangle2.length = int(input())
rectangle2.width = int(input())

rectangle1.print_length_width('First rectangle >>>> ')
rectangle2.print_length_width('Second rectangle >>>> ')



class PressureRegulator:
    minimal_pressure = 45
      
    def __init__(self):
        self.recorded_pressure = self.minimal_pressure
  
    def set_pressure(self, valve_pressure):

        if valve_pressure > PressureRegulator.minimal_pressure:
            self.recorded_pressure = valve_pressure
  
pressure_regulator_data1 = PressureRegulator()
pressure_regulator_data1.set_pressure(int(input()))
print(f'Pressure adjusted at time 1: {pressure_regulator_data1.recorded_pressure}')

pressure_regulator_data2 = PressureRegulator()
pressure_regulator_data2.set_pressure(int(input()))
print(f'Pressure adjusted at time 2: {pressure_regulator_data2.recorded_pressure}')



class ApplePie:
    total_pies = 0
    
    def __init__(self):
        self.num_apples = 0

    def cook(self, apples_used):

        ApplePie.total_pies += 1
        self.num_apples = apples_used
        print(f'One apple pie made with {self.num_apples} apples')
    
total_apples_used = 0
for token in input().split():
    apple_pie = ApplePie()
    apple_pie.cook(int(token))
    total_apples_used += apple_pie.num_apples
print(f'Number of apple pies made: {ApplePie.total_pies}')
print(f'Total number of apples used: {total_apples_used}')





class Seat:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def reserve(self, f_name, l_name, amt_paid):
        self.first_name = f_name
        self.last_name = l_name
        self.paid = amt_paid

    def make_empty(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def is_empty(self):
        return self.first_name == ''

    def print_seat(self):
        print(f'{self.first_name} {self.last_name}, Paid: {self.paid:.2f}')


def make_seats_empty(seats):
    for s in seats:
        s.make_empty()


def print_seats(seats):
    for i in range(len(seats)):
        print(f'{i}:', end=' ')
        seats[i].print_seat()

num_seats = 5

available_seats = []
for i in range(num_seats):
    available_seats.append(Seat())

command = input('Enter command (p/r/q):\n')
while command != 'q':
    if command == 'p':  # Print seats
        print_seats(available_seats)
    elif command == 'r':  # Reserve a seat
        seat_num = int(input('Enter seat num:\n'))
        if not available_seats[seat_num].is_empty():
            print('Seat not empty')
        else:
            fname = input('Enter first name:\n')
            lname = input('Enter last name:\n')
            paid = float(input('Enter amount paid:\n'))
            available_seats[seat_num].reserve(fname, lname, paid)
    else:
        print('Invalid command.')

    command = input('Enter command (p/r/q):\n')


class RaceTime:
    def __init__(self, start_time, end_time, distance):
        """
         start_time: Race start time. String w/ format 'hours:minutes'.
         end_time: Race end time. String w/ format 'hours:minutes'.
         distance: Distance of race in miles.
        """
    # ...

# The race times of marathon contestants
time_jason = RaceTime('3:15', '7:45', 26.21875)
time_bobby = RaceTime('3:15', '6:30', 26.21875)


class RaceTime:

    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        print(f'Time to complete race: {hours}:{minutes}')

    def print_pace(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        total_minutes = hours*60 + minutes
        print(f'Avg pace (mins/mile): {total_minutes / self.distance:.2f}')

distance = 5.0

start_hrs = int(input('Enter starting time hours: '))
start_mins = int(input('Enter starting time minutes: '))
end_hrs = int(input('Enter ending time hours: '))
end_mins = int(input('Enter ending time minutes: '))

race_time = RaceTime(start_hrs, start_mins, end_hrs, end_mins, distance)

race_time.print_time()
race_time.print_pace()


class Employee:
    def __init__(self, name, wage=8.25, hours=20):
        """
        Default employee is part time (20 hours/week)
        and earns minimum wage
        """
        self.name = name
        self.wage = wage
        self.hours = hours

    # ...


todd = Employee('Todd')  # Typical part-time employee
jason = Employee('Jason')  # Typical part-time employee
tricia = Employee('Tricia', wage=12.50, hours=40)  # Manager employee

employees = [todd, jason, tricia]

for e in employees:
    print (f'{e.name} earns {e.wage*e.hours:.2f} per week')
    
    
    
    
class Voicemail:

    def __init__(self, name, number, greeting="Leave a message"):
        self.name = name
        self.number = number
        self.greeting = greeting

name2 = input()
number2 = int(input())
greeting2 = input()

default_voicemail = Voicemail('Fay', 678456)
voicemail2 = Voicemail(name2, number2, greeting2)

print(f"Default voicemail data: {default_voicemail.name}'s inbox, {default_voicemail.number}, {default_voicemail.greeting}")
print(f"voicemail2 data: {voicemail2.name}'s inbox, {voicemail2.number}, {voicemail2.greeting}")



class RaceTime:
    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):
        total_time = self._diff_time()
        print(f'Time to complete race: {total_time[0]}:{total_time[1]}')

    def print_pace(self):
        total_time = self._diff_time()
        total_minutes = total_time[0]*60 + total_time[1]
        print(f'Avg pace (mins/mile): {total_minutes / self.distance:.2f}')

    def _diff_time(self):
        """Calculate total race time. Returns a 2-tuple (hours, minutes)"""
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        return (hours, minutes)


distance = 5.0

start_hrs = int(input('Enter starting time hours: '))
start_mins = int(input('Enter starting time minutes: '))
end_hrs = int(input('Enter ending time hours: '))
end_mins = int(input('Enter ending time minutes: '))

race_time = RaceTime(start_hrs, start_mins, end_hrs, end_mins, distance)

race_time.print_time()
race_time.print_pace()



class Toy:
    def __init__(self, name, price, min_age):
        self.name = name
        self.price = price
        self.min_age = min_age
        
    # similar to Javas toString()
    def __str__(self):
        return (f'{self.name} costs only ${self.price:.2f}. Not for children under {self.min_age}!')

truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)




class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        return (
            f'{self.year} {self.make} {self.model}: \n\t'
            f'Mileage: {self.miles} \n\t'
            f'Sticker price: ${self.price}'
            )

cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Maxima', 2012, 25000, 15750))

for car in cars:
    print(car)



class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.hours}:{self.minutes}'

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

num_times = 3
times = []

# Obtain times from user input
for i in range(num_times):
    user_input = input('Enter time (Hrs:Mins): ')
    tokens = user_input.split(':')
    times.append(Time(int(tokens[0]), int(tokens[1])))

min_time = times[0]
for t in times:
    if t < min_time :
        min_time = t

print(f'\nEarliest time is {min_time}')

#In the above program, the Time class contains a definition for the __lt__ method, 
#which overloads the < operator. When the comparison t < min_time is evaluated, 
#the __lt__ method is automatically called. The self parameter of __lt__ is bound 
#to the left operand, t, and the other parameter is bound to the right operand, 
#min_time. Returning True indicates that t is indeed less than min_time, and 
#returning False indicates that t equal to or greater than min_time.

#Methods like __lt__ above are known as rich comparison methods. The following 
#table describes rich comparison methods and the corresponding relational operator 
#that is overloaded.

Rich comparison method	    Overloaded operator
__lt__(self, other)	        less than (<)
__le__(self, other)	        less than or equal to (<=)
__gt__(self, other)	        greater than (>)
__ge__(self, other)	        greater than or equal to (>=)
__eq__(self, other)	        equal to (==)
__ne__(self, other)	        not equal to (!=)




class Quarterback:
    def __init__(self, yrds, tds, cmps, atts, ints, wins):
        self.wins = wins

        # Calculate quarterback passer rating (NCAA)
        self.rating = ((8.4*yrds) + (330*tds) + (100*cmps) - (200 * ints))/atts

    def __lt__(self, other):
        if (self.rating < other.rating) or (self.wins < other.wins):
            return True
        return False

    def __gt__(self, other):
        if (self.rating > other.rating) and (self.wins > other.wins):
            return True
        return False
        

peyton = Quarterback(yrds=4700, atts=679, cmps=450, tds=33, ints=17, wins=10)
print(peyton.rating)
eli = Quarterback(yrds=4002, atts=539, cmps=339, tds=31, ints=25, wins=9)
print(eli.rating)
tom = Quarterback(yrds=4806, atts=578, cmps=398, tds=50, ints=8, wins=16)
print(tom.rating)


if peyton > eli:
    print('Peyton is better than eli')
    if peyton > tom:
        print('Peyton is also better than Tom')
    else:
        print("But he isn't better than Tom")
elif peyton < eli:
    print('Eli is better than peyton')
else:
    print('It is not clear who the better QB is...')



class CarRecord:
    def __init__(self):
        self.year_made = 0
        self.car_vin = ''

    # FIXME add __str__()

    def __str__(self):
        return (
                f'Year: {self.year_made}, '
                f'VIN: {self.car_vin}'
                )
                

my_car = CarRecord()
my_car.year_made = int(input())
my_car.car_vin = input()

print(my_car)


MORE OPERATOR OVERLOADING

Method	                    Description
__add__(self, other)	    Add (+)
__sub__(self, other)	    Subtract (-)
__mul__(self, other)	    Multiply (*)
__truediv__(self, other)	Divide (/)
__floordiv__(self, other)	Floored division (//)
__mod__(self, other)	    Modulus (%)
__pow__(self, other)	    Exponentiation (**)
__and__(self, other)	    "and" logical operator
__or__(self, other)	        "or" logical operator
__abs__(self)	            Absolute value (abs())
__int__(self)	            Convert to integer (int())
__float__(self)	            Convert to floating point (float())


class Time24:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f'{self.hours:02d}:{self.minutes:02d}'

    def __gt__(self, other): 
        if self.hours > other.hours: 
            return True 
        else: 
            if self.hours == other.hours: 
                if self.minutes > other.minutes: 
                    return True 
        return False

    def __sub__(self, other):
        if isinstance(other, int): # is right op an integer ex: time1 - 1
            return Time24(self.hours - other, self.minutes)

        if isinstance(other, Time24):  # right op is Time24
            if self > other:
                larger = self
                smaller = other
            else:
                larger = other
                smaller = self

            hrs = larger.hours - smaller.hours
            mins = larger.minutes - smaller.minutes
            if mins < 0:
                mins += 60
                hrs -=1

            # Check if times wrap to new day
            if hrs > 12:
                hrs = 24 - (hrs + 1)
                mins = 60 - mins

            # Return new Time24 instance
            return Time24(hrs, mins)

        print(f'{type(other)} unsupported')
        raise NotImplementedError

t1 = input('Enter time1 (hours:minutes): ')
tokens = t1.split(':')
time1 = Time24(int(tokens[0]), int(tokens[1]))
t2 = input('Enter time2 (hours:minutes): ')
tokens = t2.split(':')
time2 = Time24(int(tokens[0]), int(tokens[1]))

print(f'Time difference: {time1 - time2}'