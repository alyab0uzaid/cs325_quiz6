from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

def main():
    # Dummy values
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 6)

    # Calculating areas
    print("Circle Area:", circle.get_area())
    print("Square Area:", square.get_area())
    print("Rectangle Area:", rectangle.get_area())

if __name__ == "__main__":
    main()
