# Variable = A container for a value (string, integer, float, boolean)
# A Variable acts as if it was the value it contains

#string: Texts or messages
first_name = "Nattawut"
food = "Pizza"
email = "nattawut123@mail.com"
print(first_name)
print(f"Hello, {first_name}")
print(f"I like {food}")
print(f"My email is {email}")

#Integers: a whole FULL numbers
age = 25
quantity = 3
num_of_students = 30
print(f"I am {age} years old.")
print(f"I am buying {quantity} items.")
print(f"My class have {num_of_students} students.")

# Float: floating point number, Decimal portion
price = 10.99
gpa = 3.46
distance = 5.5
print(f"The price is ${price}")
print(f"My gpa is: {gpa}")
print(f"I ran {distance} KM.")

#Boolean: True or False
is_student = False
for_sale = False
is_online = True
print(f"Are you a student ? {is_student}")

# If-clause Statement: is_student
if is_student:
    print("you a student.")
else:
    print("you are NOT a student.")
# If-clause Statement: for_sale
if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT available.")
# if-clause Statement: is_online
if is_online:
    print("You are online.")
else:
    print("You are offline.")

