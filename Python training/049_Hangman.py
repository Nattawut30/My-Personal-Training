# Hangman in Python
import random
# from wordslist import words <= if you want more words. import lists from somewhere else

words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key:()
hangman_art = {0: ("    ",
                   "    ",
                   "    "),
               1: (" o ",
                   "    ",
                   "    "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\ ", # you need 2 back-slash to print \
                   "   "),
               5: (" o ",
                   "/|\\ ", # you need 2 back-slash to print \
                   "/  "),
               6: (" o ",
                   "/|\\ ", # you need 2 back-slash to print \
                   "/ \\ ")}

def display_man(wrong_guesses):
    print("*" * 12)
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*" * 12)

def display_hint(hint):
    print(" ".join(hint)) # for each chars within our hint, join it by an empty space

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    print(hint)
    wrong_guesses = 0
    guessed_letter = set()
    is_running = True

    # It's True by defaults
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha(): # alphabetical chars = True, If not = False
            print("Invalid Input")
            continue

        if guess in guessed_letter:
            print(f"{guess} already guessed")
            continue

        guessed_letter.add(guess) # Keep track the letter that we already guessed

        if guess in answer:
            for i in range(len(answer)): # i = index for short.
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1 # add +1 elements of hangman

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False # Exist the loop

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()