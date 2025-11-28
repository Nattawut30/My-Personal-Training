# Python reading files (.txt, .json, .csv)

file_path = "/Users/nattawut/PycharmProjects/PythonProject/output.txt"

try:
    with open(file_path, mode="r") as file: # R = Read
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError: # If you don't have a permission to read that file.
    print("Permission denied!") # Break it

# Let's try to read the .json file

import json

file_path = "/Users/nattawut/PycharmProjects/PythonProject/output.json"

try:
    with open(file_path, mode="r") as file: # R = Read
        content = json.load(file) # Assign our variable of content equal to access to JSON modules
        print(content) # You can find specific like print(content[name])
except FileNotFoundError:
    print("That file was not found!")
except PermissionError: # If you don't have a permission to read that file.
    print("Permission denied!") # Break it

# Next is read .CSV file

import csv

file_path = "/Users/nattawut/PycharmProjects/PythonProject/output.csv"

try:
    with open(file_path, mode="r") as file: # R = Read
        content = csv.reader(file)
        for line in content:
            print(line) # Find a specific index print(line[0])
except FileNotFoundError:
    print("That file was not found!")
except PermissionError: # If you don't have a permission to read that file.
    print("Permission denied!") # Break it