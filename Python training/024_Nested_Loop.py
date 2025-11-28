#          nested loop = A loop within another loop (outer, inner)
#          outer loop:
#               inner loop:

# Basics concept of nested loop.
for x in range(3): # Outer loop
    for y in range(1, 10): # Inner loop
        print(y, end="")
    print()

# Another example of tables by nested loop
rows = int(input("Enter The # of rows: "))
columns = int(input("Enter The # of columns: "))
symbol = input("Enter The Symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
