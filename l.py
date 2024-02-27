from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

class Polygon(Shape):
    def __init__(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length

    def get_area(self):
        # Area calculation logic for polygon
        # Implement area calculation based on polygon properties
        pass

def main():
    # Dummy values
    rectangle = Rectangle(3, 4)
    circle = Circle(5)
    triangle = Triangle(4, 5)
    polygon = Polygon(6, 4)

    # Calculating areas
    print("Rectangle Area:", rectangle.get_area())
    print("Circle Area:", circle.get_area())
    print("Triangle Area:", triangle.get_area())
    print("Polygon Area:", polygon.get_area())

if __name__ == "__main__":
    main()
