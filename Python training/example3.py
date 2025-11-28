# This file is part of 045_if name == 'main'.py
# Use this file with example3.py

#print(dir())

# * means import everything
from example2 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

# Use this to define 'main' function
def main():
    print("This is example3")
    favorite_food("sushi")
    favorite_drink("coffee")
    print("Goodbye!")

# Put this at the end of the code
if __name__ == "__main__":
    main()

# Basically, It linked files together by recall it for one another
# linked file example2.py to this by import them here