# Variable Scope = where a variable is visible and accessible
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Functions can't see inside the others functions
# Local = located the variable in function first

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()

from math import e # This is Global, it's a standard
# Global e = 2.718281828459045

def func3():
    print(e)

e = 3 # Built-In e = 3 that we set up by ourselves
func3()
# Built-In is what we make it owns
