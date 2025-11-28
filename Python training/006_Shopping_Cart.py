# Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many items would you like to buy?: "))
total = price * quantity

print(f"You have bought {quantity} X {item}/s")
print(f"Your total is ${total}")
