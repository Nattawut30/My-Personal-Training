# Collection = single "Variable" used to store multiple values
# List =    [] ordered and changeable. Duplicates OK
# Set =     {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple =   () ordered and unchangeable. Duplicates OK. FASTER

# 01: List []
fruits = ["apple", "orange", "banana", "coconut"]
print(fruits[:3])

print()

# We can use it on the Loop
for fruit in fruits:
    print(fruit)

print()

# Functions
print(len(fruits))
# print(dir(fruits))
# print(help(fruits))

print()

# Check object on the List
print("pineapple" in fruits)
# pineapple is not a list so it's false

print()

# Replace subject in the List
fruits[1] = "pineapple"
for fruit in fruits:
    print(fruit)
# 1 is "orange" replace with "pineapple" instead

print()

# You can do this as well LIST []

# fruits.append("pineapple") = add elements at the end of the list
# fruits.remove("apple") = remove the elements in the list
# fruits.insert(0, "pineapple") = insert the elements at 0 (first) on the list
# fruits.sort() = sort the order of the list
# fruits.reverse() = reverse the order that place them
# fruits.clear () = all the elements in the list are gone
# print(fruit.index("apple"))= return an index of the elements on the list
# print(fruits.count("banana")) = count the elements in the list as required

# 02: Set {}
my_fruits = {"apple", "orange", "banana", "coconut", "coconut"}
# You can see it's not in orders
# Also, cannot add a copy or duplicates of element

# my_fruits.add("pineapple")
# my_fruits.remove("apple")
# my_fruits.pop() = remove whatever element is first. but it's random.
# my_fruits.clear()

print(my_fruits)

print()

# 03: Tuple ()
your_fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(your_fruits)

print(your_fruits.index("apple"))
print(your_fruits.count("coconut"))
# for loops is work well
for your_fruit in your_fruits:
    print(your_fruit)