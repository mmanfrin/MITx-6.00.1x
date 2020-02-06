# Exercise: iter power

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 6 minutes

# Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication.
# For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.

# This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical
# value. Your code must be iterative - use of the ** operator is not allowed.

def iterPower(base, exp):
    """Calculate Power with iteration
    
    Arguments:
        base {int or float} -- base of operation
        exp {power} -- exponential power
    
    Returns:
        int or float -- result of operation
    """    
    
    result = 1
    for i in range(exp):
        result *= base
    return result
        
print(iterPower(4, 2))