# super() = Function used in a child class (sub-class) to call methods from a parent class (super-class).
#           Allows you to extend the functionality of the inherited methods


# Parent class
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'unfilled'}.")

# Children class
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) #Inherit this from parent, make it simpler
        self.radius = radius

    def describe(self):
        print(f"It is circle with an area of {3.14 * self.radius * self.radius:.2f} cm^2.")
        # Methods overwriting
        # If the child class shares a similar method with a parent,
        # BUT WILL USE the child's version and not the parents version!
        # It's called method overriding

        super().describe()
        # Recall parent functions

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled) # Used super() to recall parent functions
        self.width = width

    def describe(self):
        print(f"It is square with an area of {self.width * self.width} cm^2.")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled) # Used this to re-use the function from parent class
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is Triangle with an area of {self.width * self.height / 2} cm^2.")
        super().describe() # Assign an attribute the all of its sibling have in common

circle = Circle(color="Red", is_filled=True, radius=5)
square = Square(color="Blue", is_filled=False, width=6)
triangle = Triangle(color="Yellow", is_filled=True, width=7, height=8)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius} cm.")
print()

print(square.color)
print(square.is_filled)
print(f"{square.width} cm.")
print()

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width} cm.")
print(f"{triangle.height} cm.")
print()

circle.describe()
square.describe()
triangle.describe()