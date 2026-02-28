'''
    This is a child class that inherits from the parent class Shape
'''
import math
from shape import Shape

class Circle(Shape): # Inherits from Shape -- Child class
    # The super().__init__ construct passes any parameters that are needed by the parent class.
    def __init__(self, radius, color='black'):
        super().__init__(color)

        # Set the values of the private fields for this instance of the class.
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius * self.__radius
    
    def perimeter(self):
        return 2 * math.pi * self.__radius