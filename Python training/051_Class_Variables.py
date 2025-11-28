# class variables

# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from the class

class Student:

    # You can access class variable anywhere
    class_year = 2023
    num_students = 0

    def __init__(self, name, age): #self refers to objects we're currently working with.
        self.name = name
        self.age = age
        Student.num_students += 1 # access on the shared variables

# Variables are shared among all instances of a class

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 25)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(Student.num_students)
print()

print(student1.name)
print(student1.age)
print(Student.class_year)
print()

print(student2.name)
print(student2.age)
print(Student.class_year)
print()

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
print()

# It's Allow you to share data among all objects created from that class