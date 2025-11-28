# Python Number Guessing Game
# practice of random functions

import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number,highest_number)
guesses = 0
is_running = True

print("---------- Python Number Guessing Game Project ----------")
print(f"Select a number between {lowest_number} and {highest_number}")


while is_running: # Set default is True so the player can continue playing

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess) #Tranform their answer to be a number not string
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print("Your number is out of range.")
            print(f"Please select a  number between {lowest_number} and {highest_number}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The number was {answer}.")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess.")
        print(f"Please select a  number between {lowest_number} and {highest_number}")