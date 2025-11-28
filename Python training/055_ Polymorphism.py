# polymorphism = Greek word that means to "have many forms or faces"
#               Poly = Many
#               Morphe = Form

#               TWO WAYS TO ACHIEVE POLYMORPHISM
#               1. Inheritance = an object could be treated of the same type as a parent class
#               2. "Duck typing" = object must have necessary attributes/methods

from abc import ABC, abstractmethod

# Parent class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Children class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

# Pizza is NOT inherit from parent class
# But somehow It's look like a circle...
# So, we assign it on one of the sibling class

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius) #Calls the radius attribute from circle

# Now, our Pizza is considered 3 forms
# 1. A pizza
# 2. A circle
# 3. A shape

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("Pepperoni", 15)]
# A Pizza is inside the deep folders category of shape, it's also a circle as well.

for shape in shapes:
    print(f"{shape.area()} cm²")
    # Window = Alt + 0178, Mac = Control + Command + Space for ^2

# Somehow most of the functions is look like a deep folders
# They're the sub-set of one another
# Keeps stacking in function