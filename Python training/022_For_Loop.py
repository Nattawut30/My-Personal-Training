#          For loops = execute a block of code a fixed number of times.
#          You can iterate over a range, string, sequence, etc.

# Keep 1 but not 11, only get 10
for x in range(1, 11):
    print(x)

print()

# Reversed function
for x in reversed(range(1, 11)):
    print(x)
print("Happy New Year!")

print()

# Count the number 1-10 but count by 2
for x in range(1, 11, 2):
    print(x)

print()

# Credit Cards
credit_card = "1234-5677-9012-3456"
for x in credit_card:
    print(x)

print()

# Use "Break" stop at 13
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# Different from the "While Loop" is that While Loop is want to get in a infinity loops
# meanwhile "For Loops" has a fixed range and achieved the determined range.

