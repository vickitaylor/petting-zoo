class Product:

    @property #the getter
    def price(self):
        try:
            return self.__price
        except AttributeError:
            return 0

    @price.setter #the setter
    def price(self, new_price):
        if type(new_price) is float:
            self.__price = new_price
        else:
            raise TypeError('Please provide a floating point value for the price')


class Serial:
    def __init__(self, serial_num):
        self.__serial_num = serial_num #setting the privately scoped attribute on instantiation

    @property #the getter
    def serial_num(self):
        return self.__serial_num # now foo.serial_num will actually return the private value. 
                                 # There is no actual serial_num attribute.


    @serial_num.setter #the setter
    def serial_num(self, number):
        pass # here, we simply tell the function to do nothing, effectively preventing the setting
             #  of a value for .serial_num. Without the setter, though, an attempt to assign a value
             # to foo.serial_num would throw an Attribute Error and break stuff.

class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
