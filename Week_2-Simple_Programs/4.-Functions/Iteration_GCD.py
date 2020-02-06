# Exercise: gcd iter

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,
# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1

# Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to
# the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test
# divides both a and b without remainder, or you reach 1.

def gcdIter(a, b):
    """search fod the GCD
    
    Arguments:
        a {int} -- 1st number
        b {int} -- 2nd number
    """    
    # Your code here
    
    z = min(a, b)
        
    for i in range(z, 0 , -1): #decrescent search for GCD
        if a % i == 0 and b % i == 0:
            return i
    
    
a = 120
b = 664
print(gcdIter(a, b))