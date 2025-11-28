# Python Slot Machine Exercise

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    # Much better options
    return [random.choice(symbols) for _ in range(3)]
    # _ as a placeholder, every iteration in range three, return a random symbol

def print_row(row):
    print("*" * 15)
    print("|".join(row))
    print("*" * 15)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20

    return 0

def main():
    balance = 100

    print("*" * 30)
    print("Welcome to Python Slots")
    print("Symbol: 🍒 🍉 🍋 🔔 ⭐️") # Control + Command + Space = Emoji
    print("*" * 30)

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue # will skip the current iteration of this loop and start from the beginning

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("*" * 30)
    print(f"Game Over! your final balance is ${balance}")
    print("*" * 30)



if __name__ == "__main__":
    main()