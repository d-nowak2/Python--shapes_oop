'''
    This is our main Shape class. It contains methods that define the name of the method (area and perimeter) but 
    not the method functionality--that is left to the individual shape classes.
'''

class Shape: # Parent class
    def __init__(self, color='black'):  # Initializer --> Constructor Method
        self.__color = color            # private field (Encapsulation) -- Name Mangled: __ClassName__fieldName
        self.notes = []                 # public field

    # A property is a way to expose the data in a private field.
    @property
    def color(self):
        return self.__color
    
    # Meant to be Overriden by the specific shape classes.
    def area(self):
        return 0
    
    # Optional Override for optional implementation in the specific shape classes.
    def perimeter(self):
        return 0
    
    # The Dunder __str__ method provides the functionality for when we print a class instance.
    # For example, in main, if we print(rectangle) this is the method that will be called to print the values of the rectangle.
    def __str__(self):
        return f'{self.__class__.__name__} (color={self.color}) area={self.area():.2f} perimeter={self.perimeter():.2f}'