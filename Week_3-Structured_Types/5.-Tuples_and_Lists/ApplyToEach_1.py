def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def absolute(a):
    return abs(a)

applyToEach(testList, absolute)