# While loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

# Remains True, execute this code.
# If it's False, you exit out of the while loop
while name == "":
    print("You did not enter a name")
    name = input("Enter your name: ") #Give them some chance to escape the loop

print(f"Hello, {name}")

# Ex.2
age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")

# Ex.3
food = input("Enter a food you like (q to quit): ")
while not food == "q":
    print(f"You like {food}!")
    food = input("Enter another food you like (q to quit): ")

print("Bye.")

# Ex.4
num = int(input("Enter a number # between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not a valid number.")
    num = int(input("Enter a number # between 1 - 10: "))

print(f"Your number is {num}.")




