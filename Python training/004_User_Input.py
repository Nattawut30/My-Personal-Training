# input() = A function that prompts the user to enter data
# Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("What is your age?: ")) #Change its contains Values as Integers

age = age + 1

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print("Happy Birthday!")

# Don't forget: The values contains as String by defaults.