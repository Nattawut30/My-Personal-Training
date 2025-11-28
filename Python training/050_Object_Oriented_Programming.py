# Object-Oriented Programming

# Object = A "bundle" of related attributes (variables) and methods (function)
#          Ex.
#          Phone (def make_call():, receive_call, turn_on),
#          Cup (def fill_cup():, drink_cup, empty_cup),
#          Book (def open_book():, read_book, close_book)

#          You need a "Class" to create many objects

# Class =  (blueprint) used to design the structure and layout of an object

# IMO: Sound like a big sub-set in math

# you can place it another Python files and import somewhere else
class Car: #We need constructor
    def __init__(self, model, year, color, for_sale):#Dunder = double underscore __
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model} {self.year} {self.color}")

    def stop(self):
        print(f"you stop the {self.model} {self.year} {self.color}")

    def describe(self):
        print(f"{self.model} {self.year} {self.color}")

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)


# dot is known as the attribute access operator
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
print()

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
print()

# It's good for organized, and cleaner.

# Applied with the def functions
car1.drive()
car2.drive()
car3.drive()
print()

car1.stop()
car2.stop()
car3.stop()
print()

car1.describe()
car2.describe()
car3.describe()
print()