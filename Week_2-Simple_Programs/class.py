def recurPower(base, exp):
    """Calculate Power with recursion
    
    Arguments:
        base {int or float} -- base of operation
        exp {power} -- exponential power
    
    Returns:
        int or float -- result of operation
    """    
    
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
        
print(recurPower(2, 0))