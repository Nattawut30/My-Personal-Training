# Multiple inheritance = Inherit from more than one parent class
#                       C(A, B)

# Multilevel inheritance = inherit from a parent which inherits from another parent
#                        C(B) < - B(A) < - A

#                       It's look like a stacked

# Parents Classes
# Parent can inherit another parent
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} Eating")

    def sleep(self):
        print(f"{self.name} Sleeping")
# Think of class Animal as grand-parent

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# Children Classes
# If inherit from prey, they get the ability to flee
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
print()

# The function inside another multiple level of inheritance

rabbit.eat()
rabbit.sleep()
fish.eat()
fish.sleep()
hawk.eat()
hawk.sleep()