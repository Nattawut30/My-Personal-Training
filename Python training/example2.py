# This file is part of 045_if name == 'main'.py
# Use this file with example3.py

def favorite_food(food):
    print(f"Your favorite food is {food}")

# use this to define 'main' function
def main():
    print("This is example2")
    favorite_food("Pizza")
    print("Goodbye!")

# Put this at the end of the code
if __name__ == "__main__":
    main()

# Basically, It linked files together by recall it for one another
# This file uses it as an own set-up file to import to somewhere (example3.py)

