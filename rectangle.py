'''
    This is a child class that inherits from the parent class Shape
'''
from shape import Shape 

class Rectangle(Shape): # Inherits from Shape -- Child class
    # This is the initializer method for this class.
    def __init__(self, width, height, color='black'):
        # The super().__init__ construct passes any parameters that are needed by the parent class.
        super().__init__(color)

        # Set the values of the private fields for this instance of the class.
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        return 2 * (self.__width + self.__height)