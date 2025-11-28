# Module = a file containing code you want to include in your program
#        use 'import' to include a module (built-in on your own)
#        useful to break up a large program reusable separate files
#        ---- main files + Owns Modules ----
#print(help("modules"))

import math
import math as m
from math import pi
from math import e
a, b, c, d, e = 1, 2, 3, 4, 5
print(pi)
print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)
print()

# you can set up or make your own files and then import
# Imagine this is main.py, then import our owns file here
import example #This is my example file, import it here

a = example.pi
b = example.square(3)
c = example.cube(3)
d = example.circumference(3)
e = example.area(3)

print(a)
print(b)
print(c)
print(d)
print(e)
print()
