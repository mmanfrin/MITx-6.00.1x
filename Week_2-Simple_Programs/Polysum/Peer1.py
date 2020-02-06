import math
def polysum(n, s):
    '''
        input: two numbers: n-number of sides, s - the length of side
        output: one number rounded to 4 decimal digits precision - the sum of square of the perimeter and the area 
    '''
    return n*s + round(0.25*n*s*s/math.tan(math.pi/n), 4)

