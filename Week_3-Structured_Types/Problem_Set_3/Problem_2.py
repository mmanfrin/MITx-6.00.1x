def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ''
    for i in secretWord:
        if i in lettersGuessed:
            guess += i
        else:
            guess += ' _ '
    print('')
    
    return guess


secretWord = 'apple' 
lettersGuessed = ['l', 'i', 'k', 'a', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
# '_ pp_ e'