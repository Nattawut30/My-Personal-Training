# Membership Operators = used to test whether a value or variable is found in a sequence
#                      (string, list, tuple, or dictionary)
#                       1. in
#                       2. not in

#String
word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There's a {letter}")

#Set
students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the student's name: ")
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

#Dictionary
grades = {"Sandy": "A",
          "Squidward": "B",
          "Spongebob": "C",
          "Patrick": "D"}
student = input("Enter the student's name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

#
email = "nattawut@gmail.com"

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")






