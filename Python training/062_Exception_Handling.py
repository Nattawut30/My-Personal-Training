# exception = An event that interrupts the flow of a program
#           = (ZeroDivisionError, TypeError, ValueError)
#           = 1. Try, 2. Except, 3. Finally

# Seems like we put some rules on the program
# If something is go wrong from out rules then it's stop

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")

