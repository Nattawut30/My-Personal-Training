# Python Writing Files (.txt, .json, .csv)
# Use this file with output.txt

employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "output.txt"

try:
    with open(file=file_path, mode="w") as file: # W = write, A = append, R = Read
        for employee in employees:
            file.write(" " + employee) # \n means new line character
        print(f"txt file '{file_path}' was created")
except FileNotFoundError:
    print(f"file '{file_path}' already exists")

# The file output.txt is now created on Python directory

# You can add it on your desktop
# file_path = /Users/nattawut/Desktop

# Below is .json file
# Use this file with output.json

import json

person = {
    "name": "Eugene",
    "age": 30,
    "job":"Cook"
}

file_path = "output.json"

try:
    with open(file=file_path, mode="w") as file: # W = write, A = append, R = Read
        json.dump(person, file, indent=4) # will convert our dictionary to a JSON string to output it
        # indent = for each values pair, how many spaces do we want to indent each?
        print(f"json file '{file_path}' was created")
except FileNotFoundError:
    print(f"file '{file_path}' already exists")

# Now it's CSV files or some kind of spreadsheet
# Use this file with output.csv

import csv

human = [
    ["Name", "Age", "Job"],
    ["Spongebob", 30, "Cook"],
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]

file_path = "output.csv"

try:
    with open(file=file_path, mode="w", newline="") as file: # W = write, A = append, R = Read
        writer = csv.writer(file) # Writer is an object. It's methods for writing data for a CSV file.
        for row in employees:
            writer.writerow(row) # Pass in the row that we're iterating over.
        print(f"csv file '{file_path}' was created")
except FileNotFoundError:
    print(f"file '{file_path}' already exists")

