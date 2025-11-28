# 2 Dimension of collections

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

# make it rows and columns
groceries = [fruits, vegetables, meats]
print(groceries[2][2]) # Rows 1:Column 0
# don't forget the first elements is start with '0'

print()

# Applied for loop
for collection in groceries:
    print(collection)

print()

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print() # make them printing new line

print()

# Ex. 2
num_pad = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9),
          ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print() # make them printing new line
