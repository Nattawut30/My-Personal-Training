# Python Banking Program

# 1. Show Balance
# 2. Deposit
# 3. Withdraw

# Define banking methods (Menu of the category)
def show_balance(balance):
    print(f" Your balance is ${balance:.2f}")
    print("*" * 12)

def deposit():
    amount = float(input("Enter amount to deposit: "))
    print("*" * 12)

    if amount < 0:
        print("That's not a valid amount")
        print("*" * 12)
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    print("*" * 12)

    if amount > balance:
        print("Insufficient funds!")
        print("*" * 12)
        return 0
    elif amount < 0:
        print("Amount must be greater than 0!")
        print("*" * 12)
        return 0
    else:
        return amount

# Imagine it!
# Above is like a menu orders category first (Food, Beverage, Fruits)
# Below is like what the menu in the category offers (Pizza, Hamburger, Coca-Cola, Pepsi, Apple, Banana)
# Function is like a sub-set of the determined set

# Define the 'main' function (Inside the category)
def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("*" * 12)

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*" * 12)

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice")
            print("*" * 12)

    print("Thank you! have a nice day!")
    print("*" * 12)

# If functions is running, recall it.
if __name__ == "__main__":
    main()