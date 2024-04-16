#!/usr/bin/env python3
# Module 7
# customer.py
# represents a Customer class

import datetime
from datetime import datetime

class Customer:
    # constructor
    def __init__(self, name, strAddr):
        self.__name = name
        self.__strAddr = strAddr
        self.__creationDate = datetime.now()

# accessor/mutator for name
    @property
    def name(self):
        # print("in name getter") # debug
        return self.__name

    @name.setter
    def name(self, name):
        # print("in name setter, param=" + name) # debug
        self.__name = name
# accessor/mutator for strAddr
    @property
    def strAddr(self):
        # print("in strAddr getter") # debug
        return self.__strAddr

    @strAddr.setter
    def strAddr(self, strAddr):
        # print("in strAddr, param=" + strAddr) # debug
        self.__strAddr = strAddr

    # accessor (no mutator) for creationDate
    @property
    def creationDate(self):
        return self.__creationDate

    
