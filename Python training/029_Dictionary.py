# Dictionary = a collection of {key:value} pairs
#            ordered and changeable. No Duplicates.


capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA"))

print()

if capitals.get("Russia"):
    print("This capital exists")
else:
    print("This capital doesn't exist")

print()

capitals.update({"Germany": "Berlin"})
print(capitals)

print()

capitals.pop("China") # Use it to remove
print(capitals)
capitals.popitem() # Use it to remove the latest pairs
print(capitals)

print()

# Get all the keys
# capitals.clear() clear them all
keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

print()

# Get all the values in the method
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

print()

# Items return a dictionary object, resemble a 2D.
# items = [(), (), ()]
items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")