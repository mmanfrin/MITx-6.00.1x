animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for i in aDict.values():
        count += len(i)
    
    return count


    # count = 0
    # for value in aDict.values():
    #     for v in value:
    #      count  += 1
    # return count

print(how_many(animals))
# >>> 6