#          Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#          Print or assign one of two values based on a condition
#          Return X if condition is True, else return Y

num = 6
a = 6
b = 7
age = 25
temperature = 34
user_role = "admin"

# Ex. 1
print("Positive" if num > 0 else "Negative")

# Ex. 2
result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

# Ex. 3
max_num = a if a > b else b
print(max_num)

# Ex. 4
min_num = a if a < b else b
print(min_num)

# Ex. 5
status = "Adult" if age >= 18 else "Child"
print(status)

# Ex. 6
weather = "HOT" if temperature >= 25 else "COLD"
print(weather)

# Ex. 7
access_level = "Access granted." if user_role == "admin" else "Access Denied."
print(access_level)








