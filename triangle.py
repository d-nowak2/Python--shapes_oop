'''
    This is a child class that inherits from the parent class Shape
'''
from shape import Shape

class Triangle(Shape): # Inherits from Shape -- Child class
    def __init__(self, base, height, color='black'):
        # The super().__init__ construct passes any parameters that are needed by the parent class.
        super().__init__(color)

        # Set the values of the private fields for this instance of the class.
        self.__base = base
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height