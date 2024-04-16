#!/usr/bin/env python3
# car.py
# class representing a Car
# adapted from "Python Crash Course", Matthes 2019

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.__make = make      # read-only
        self.__model = model    # read-only
        self.__year = year      # read-only
        self.__odometer_reading = 0

    # getters
    
    @property
    def make(self):
        return self.__make

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def odometer_reading(self):
        return self.__odometer_reading

    # setter (only one needed, other attributes are read-only)

    @odometer_reading.setter
    def odometer_reading(self, odometer_reading):
        if odometer_reading >= self.__odometer_reading:
            self.__odometer_reading = odometer_reading
        else:
            print("You can't roll back an odometer!")

    # utility methods
    
    def get_descriptive_name(self):
        """Construct a full name from the car attributes."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a message which indicates the car odometer value."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        """Increment the car odometer using value of miles argument."""
        self.odometer_reading = self.odometer_reading + miles

# unit test
def main():
    car = Car("Dodge", "Viper SRT-10", 2010)
    print(car.get_descriptive_name())
    car.read_odometer()
    car.odometer_reading = 1000
    car.read_odometer()
    car.increment_odometer(100)
    car.read_odometer()
    car.odometer_reading = 500

if __name__ == "__main__":
    main()
