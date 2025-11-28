# Iterables = An Object/Collection that can return its elements one at a time,
#           Allowing it to be iterated over in a loop

# Normally we use this, List can be reversed
numbers = [1, 2, 3, 4 ,5]
for number in reversed(numbers):
    print(number, end="-")
print()

# Set cannot be reversed
fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
    print(fruit)
print()


name = "Nattawut Boonnoon"
for character in name:
    print(character, end=" ")
print()

# If you iterate over a dictionary,
# the dictionary is going to return all the keys not the values
my_dictionary = {"A": 1, "B": 2, "C": 3}
for values in my_dictionary.values(): #This will return all the values as variable
    print(values)
print()

for key, value in my_dictionary.items(): #Give em both key and values
    print(key, value)
    print(f"{key} = {value}")