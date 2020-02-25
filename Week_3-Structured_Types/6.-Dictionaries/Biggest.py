animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
# animals['e'] = ['eagle']
# animals['f'] = ['fox', 'flamingo', 'ferret', 'falcon']

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    val = 0
    biggest = 0
    if aDict == {}:
        val = None
    else:
        for i in aDict.keys():
            if len(aDict[i]) > biggest:
                biggest = len(aDict[i])
                val = i
    return val

print(how_many(animals))
# >>> 6