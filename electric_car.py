#!/usr/bin/env python3
# electric_car.py
# class representing an electriccar

from car import Car

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, batteryVolts = 0):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.__batteryVolts = batteryVolts   # read-only

    # getter
    @property
    def batteryVolts(self):
        return self.__batteryVolts

    # utility methods
    def get_descriptive_name(self):  # concat super's string with subclass info
        supStr = super().get_descriptive_name()
        return supStr + "\nbattery voltage = " + str(self.__batteryVolts)
    # overriding the method, not overloading
    
def main():
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla2 = ElectricCar('tesla', 'model s', 2019, 375)
    print(my_tesla2.get_descriptive_name())

if __name__ == "__main__":
    main()
