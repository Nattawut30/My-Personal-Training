# List Comprehension = A concise way to create lists in Python
#                    Compact and easier to read than traditional loops
#                    [expression for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
print()

# pattern number
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print(doubles)
print(triples)
print(squares)
print()

#string
#fruits = ["apple", "banana", "banana", "coconut"]
#fruits = [fruit.upper() for fruit in fruits]
fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)
print()

#Condition
numbers = [1, -2, 3, -4, 5, -6, 7, -8]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_num)
print(negative_num)
print(even_nums)
print(odd_nums)
print()

#Exercise
grades = [85, 42, 79, 90, 56, 61, 30, 69]
passing_grades = [grade for grade in grades if grade >= 60]

print(f"{passing_grades} passed the subject")







