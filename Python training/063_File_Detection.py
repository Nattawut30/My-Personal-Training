# Python file detection

# Use this file with test01.txt
# Use this with stuff folders
# Try it with your own system

import os #Operating System

#file_path = "stuff/test01.txt"

# You can find something in your system too
file_path = "/Users/nattawut/Desktop/"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    # We need to make sure it's a file not directory
    if os.path.isfile(file_path):
        print("That is a file")
    # dir = directory
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print(f"The location '{file_path}' doesn't exist")