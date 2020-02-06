# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is:  0.25∗n∗s2/tan(π/n) 
# The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of the 
# regular polygon. The function returns the sum, rounded to 4 decimal 
# places.

from math import tan, pi

def polysum(n, s):
    areaPol = (0.25*n*(s**2))/(tan(pi/n))
    periPol = n * s
    polySum = (areaPol + periPol**2)
    return round(polySum, 4)

n = 84
s = 10
print(polysum(n,s))