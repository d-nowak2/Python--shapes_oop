'''
    This program demonstrates an object-oriented (OOP) implementation of the classic 'shapes' example
    in Python. This main program instantiates (creates in-memory instances) of shape objects. Most of 
    the code related to shapes is found in the Shape class. But shape-specific functionality, like
    getting the area and perimeter of the shape, is found in the individual shape classes.
'''

# First, import the classes: from <file> import <ClassName>
from shape import Shape
from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle

def main():
    # Here we are constructing a list of shapes with their parameters.
    shapes = [
        Square(4, 'blue'),
        Rectangle(3, 5, 'green'),
        Circle(2.5, 'purple'),
        Triangle(6, 2, 'red'),
        Square(10),
        Shape('raspberry')]
    
    # Iterating through the list demonstrates Polymorphism: same call, different behaviors.
    for shape in shapes:
        print(shape)

if __name__ == '__main__':
    main()