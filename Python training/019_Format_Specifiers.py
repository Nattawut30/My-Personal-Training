#           format specifiers = {:flags} format a value based on what
#           flags are inserted
#
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :<  = left justify
# :>  = right justify
# :^  = center align
# :+  = use a plus sign to indicate positive value
# :=  = place sign to leftmost position
# :   = insert a space before positive numbers
# :,  = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.3478

# Ex.1 Round up the last number  .digit
print(f"price 1 is ${price1:.2f}")
print(f"price 2 is ${price2:.2f}")
print(f"price 3 is ${price3:.2f}")
print()

# Ex. 2 Each value now has a total of 10 spaces to display the output
print(f"price 1 is ${price1:10}")
print(f"price 2 is ${price2:10}")
print(f"price 3 is ${price3:10}")
print()

# Ex.3 All these numbers are now left justified. Then we have all spaces after
print(f"price 1 is ${price1:<10}")
print(f"price 2 is ${price2:<10}")
print(f"price 3 is ${price3:<10}")
print()

# Ex.4 Somehow back to defaults like Ex.2
print(f"price 1 is ${price1:>10}")
print(f"price 2 is ${price2:>10}")
print(f"price 3 is ${price3:>10}")
print()

# Ex.5 all numbers are now center
print(f"price 1 is ${price1:^10}")
print(f"price 2 is ${price2:^10}")
print(f"price 3 is ${price3:^10}")
print()

# Ex.6 Value indicator: any value that is plus+ or negative-
print(f"price 1 is ${price1:+}")
print(f"price 2 is ${price2:+}")
print(f"price 3 is ${price3:+}")
print()

# Ex.7 numbers are lined up evenly
print(f"price 1 is ${price1: }")
print(f"price 2 is ${price2: }")
print(f"price 3 is ${price3: }")
print()

# Ex.8 Each thousand's place is now separated with a comma
print(f"price 1 is ${price1:,}")
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:,}")
print()

# Ex.9 Mix and match: The combination of flags
print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:+,.2f}")
print(f"price 3 is ${price3:+,.2f}")
print()