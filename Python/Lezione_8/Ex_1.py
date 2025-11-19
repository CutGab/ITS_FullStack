# Exercise 1: Creating an Abstract Class with Abstract Methods
# Start by defining an abstract base class called Shape. This class should include two abstract methods: one named area, which will be responsible for calculating the area of a shape, and another named perimeter, which will calculate the perimeter. 
# Since Shape is abstract, it will not provide specific implementations for these methods. Instead, it sets a blueprint for all shapes that will inherit from it.

# Then, create two concrete subclasses, Circle and Rectangle, that both extend the Shape class. Each of these subclasses must provide their own implementation of the area and perimeter methods, based on the geometric formulas appropriate to their shapes.

# Finally, write a simple driver program (test code) that creates instances of Circle and Rectangle, calls their area and perimeter methods, and prints the results. This will help verify that your class hierarchy works as intended.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Circle(Shape):

    def __init__(self, raggio: float):
        super().__init__()
        self.raggio = raggio

    def area(self):

        return (self.raggio * self.raggio) * 3.14
    
    def perimeter(self):
        
        return (self.raggio * 2) * 3.14
    
class Rectangle(Shape):

    def __init__(self, base: float, altezza: float):
        super().__init__()
        self.base = base
        self.altezza = altezza

    def area(self):

        return self.base * self.altezza
    
    def perimeter(self):
        
        return (self.base + self.altezza) * 2
    
c1 = Circle(5)
r1 = Rectangle(10, 20)

print(c1.area())
print(r1.area())

print(c1.perimeter())
print(r1.perimeter())