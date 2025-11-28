# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator


# This is a decorator
def add_sprinkles(func):
    def wrapper(*args, **kwargs): # Use args and quarks to accept any number of arguments and keyword arguments
        print("*You add sprinkles 🎊")
        func(*args, **kwargs) # Then called this base function
    return wrapper # We're always need this function

# This is a decorator
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍫")
        func(*args, **kwargs) # Accept the number and arguments
    return wrapper

# Base Function
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream! 🍨")

get_ice_cream("Chocolate")