# Duck Typing = Another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/Methods
#               "If it looks like a duck and quacks like a duck, It a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

# Even Car is not an animal, but it has the minimum necessary methods
# So, It's worked too.
class Car:

    alive = False

    def speak(self): # Here, Maybe It's an AI car, we can speak as a metaphor
        print("HONK!")
    # This make Car achieve polymorphism inheritance of Animal through "Speak"
    # "If it looks like a duck, It's a duck"

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)