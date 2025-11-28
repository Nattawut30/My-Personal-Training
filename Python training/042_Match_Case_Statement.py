# Match-Case Statement (Switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable!
#                                New features added in Python 3.10+


def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: # _ means Wild Card, refers to else statement
            return "Not a valid day"

print(day_of_week(1))
print(day_of_week("Pizza"))
print()

#Ex. 2
# | means or
def is_weeked(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weeked("Sunday"))
print(is_weeked("Thursday"))
print(is_weeked("Pizza"))

# In summary: It's a if-else statements but cleaner and better