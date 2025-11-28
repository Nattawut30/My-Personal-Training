# Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

name = "Fluke"
age = 25
gpa = 3.4
is_student = True

# Casting data types
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Convert data type
gpa = int(gpa)
print(gpa)
age = float(age)
print(age)

# the same values as [age = "25"]
age = str(age)
print(type(age))

# Boolean checked: If the values is blank, it's return "False"
name = bool(name)
print(name)





