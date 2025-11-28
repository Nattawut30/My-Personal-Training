# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represent the class itself.

# Instance methods = Best for operations on instance of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # When ever we create student object, increase count by +1
        Student.total_gpa += gpa #This variable is going to accumulate all the GPA of every student

    #INSTNCE METHOD
    def get_infor(self):
        return f"{self.name} {self.gpa}"

    #CLASS METHOD
    @classmethod
    def get_count(cls): #cls = class
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls): #Always use cls for class method
        if cls.count == 0:
            return 0 #Need to return 0 values, so it's not divided by 0.
        else:
            return f"Average gpa: {cls.total_gpa/cls.count:.2f}"
        # That's how we calculate the average GPA.

student1 = Student("Spongebob", 3.46)
student2 = Student("Patrick", 2.75)
student3 = Student("Sandy", 4.00)

print(Student.get_count())
print(Student.get_average_gpa())