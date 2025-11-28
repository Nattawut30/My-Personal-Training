# Static Methods = A method that belong to a class rather than any object from that class (instance)
#                   usually used for general utility function

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    #INSTANCE METHOD
    def get_info(self):
        return f"{self.name} = {self.position}"

    #STATIC METHOD
    # No need to rely on any objects to use this method
    @staticmethod #No 'self' arguments
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

# To call, an instance method, we have to access, One ofe the instances of the class in order to use it
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(Employee.is_valid_position("Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

# For instance method you access an object, then call the instance method
# With a static method, you only need to access that class, you don't need to create any objects from that class