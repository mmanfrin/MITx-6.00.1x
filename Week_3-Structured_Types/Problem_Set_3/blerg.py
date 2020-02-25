# def isWordGuessed(secretWord, lettersGuessed): True or False
# def getGuessedWord(secretWord, lettersGuessed): apple -> a _ _ l _
# def getAvailableLetters(lettersGuessed): bcdfghjklmnpqrtuwxyz
import random
import string

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

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

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
    notGuessed = list(string.ascii_lowercase)
    
    for i in lettersGuessed:
        if i in notGuessed:
            notGuessed.remove(i)
    return ''.join(notGuessed)

# isWordGuessed = False
secretWord = ('abelha')
lettersGuessed = []

def hangman(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')

    tries = 8
    while tries > 0:
        # print(tries)
        if isWordGuessed(secretWord, lettersGuessed) == True: #check de vitória
            print('Congratulations, you won!')
            print('The word was:', secretWord)
            break
        
        else: #main checking
            print('You have', tries, 'guesses left.')
            print('Available letters:', getAvailableLetters(lettersGuessed))
            guess = str(input('Please guess a letter:')).lower()
            
            if guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
            
            else:
                lettersGuessed.append(guess)
                print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
                print('-------------')
                tries -= 1
                
                
        if tries == 0: #check de derrota
            print('Sorry, you ran out of guesses. The word was', secretWord, '.')
        
        
hangman(secretWord)
    