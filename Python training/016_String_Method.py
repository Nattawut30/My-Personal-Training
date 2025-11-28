# String methods

name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")


# len = counting how many characters in it
result = len(name)
print(result)

# find = count the first occurrence of a given characters + the position, always start with 0
result = name.find(" ")
print(result)

# rfind = r meaning reverse, find the last occurence
result = name.rfind("q")
print(result)
# -1 means no results, can't find any

# capitalize the first letter in a string
name = name.capitalize()
print(name)

# upper will take characters in a string, make them all uppercase
name = name.upper()
print(name)

# lower make them string to be a lowercase
name = name.lower()
print(name)

# isdigit, return either true or false, if string contains only digits
result = name.isdigit()
print(result)
# It is True only if I enter a number only

#isalpha, return a boolean true or false depending if a string contains only alphabetical characters
result = name.isalpha()
print(result)
# It is True only if I enter with no space

# Let's count the dash in phone number!
result = phone_number.count("-")
print(result)

# Replace the dash with something else!
phone_number = phone_number.replace("-", " ")
print(phone_number)

# Use this functions to get a methods helps
print(help(str))










