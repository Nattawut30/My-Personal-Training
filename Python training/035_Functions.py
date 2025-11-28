# Function = A block of reusable code
#          place () after the function name to invoke it

# Ex. 1
# The orders does matter.
def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_birthday("Fluke", 25)
happy_birthday("John", 35)
happy_birthday("Steve", 45)

print()

# Ex.2
def display_invoice(username, amount, due_date):
    print(f"Hello, {username}!")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Fluke", 69.99, "02/14/2025")
print()

# return = statement used to and a function
#        and send a result back to the caller

# Ex.1
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
print()

# Ex. 2

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last # Get results

full_name = create_name("king", "fluke")

print(full_name)