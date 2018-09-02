#Calculates area and circumference
#of a circle

import math

# radius
radius = float(input("Enter Radius"))

# area
area = math.pi * radius ** 2

# circumference
circumference = 2 * math.pi * radius

print (area, circumference)