'''
    This is a child class that inherits from the parent class Shape
'''
from shape import Shape

class Square(Shape): # Inherits from Shape -- Child class
    def __init__(self, side, color='black'):
        # The super().__init__ construct passes any parameters that are needed by the parent class.
        super().__init__(color)

        # Set the values of the private fields for this instance of the class.
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side