# If = Do some code IF some condition is True
# Else = do something else

# Orders of the statements matters!
age = int(input("Enter your age: "))

if age >= 100:
    print("You are a legend!")
elif age >= 18:
    print("You are legal!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are illegal!")

# Example 2
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# Example 3
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello, {name}!")

# Example 4
online = False

if online:
    print("The user is online")
else:
    print("The user is offline")
# Default values is always True