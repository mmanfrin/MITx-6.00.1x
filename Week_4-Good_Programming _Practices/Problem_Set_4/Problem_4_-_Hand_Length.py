def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    return sum(hand.values())



# XXXXXXXXX Default Config XXXXXXXXX

hand = {'a':1, 'q':1, 'b':2, 'y':2, 'e':1, 'i':1}
word = 'abbey'

# # XXXXXXXXX Output XXXXXXXXX

print(calculateHandlen(hand))