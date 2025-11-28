# Calculated circumference of the circle, C = 2 * Pi * r
import math

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")
# round functions: helps the answer is only 2 digits

# **********

# Exercise 3.2: Calculated Area of the circle, A = Pi * r²
import math

radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
# or use this: area = math.pi * radius ** 2

print(f"The area of the circle is: {round(area, 2)}cm²")

# **********

# Exercise 3.3: Calculated hypotenuse of the right triangle, C = (a² + b²)\sqrt
import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"side C = {c}")

# Mac: Control + Command + Space = ^2
