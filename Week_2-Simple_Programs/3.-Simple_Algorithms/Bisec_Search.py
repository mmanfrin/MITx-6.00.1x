x = 9
epsilon = 0.1
numGuesses = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print('pass nº ' + str(numGuesses) + ' | low = ' + str(low) + ' | high = ' + str(high) + ' | ans = ' + str(ans))
    numGuesses += 1
    
    if ans**2 < x:
        low = ans
    else:
        high = ans
        
    ans = (high + low) / 2.0
    # chk1 = abs(ans**2)
    # chk2 = abs(ans**2 - x)
    
print('numGuesses = ' + str(numGuesses))
print(str(round(ans,2)) + ' is close to square root of ' + str(x))