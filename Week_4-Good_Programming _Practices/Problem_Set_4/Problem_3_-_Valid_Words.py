WORDLIST_FILENAME = "C:/Users/Marcos/Git/MITx-6.00.1x/Week_4-Good_Programming _Practices/Problem_Set_4/wordsCopy.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # copiando dicionatio (hand)
    handVerify = hand.copy()
    
    # checa palavra na wordList
    if word in wordList:
        # loop busca/del
        for letra in word:
            # checa se existe letra no dicionario
            if letra in handVerify and handVerify[letra] > 0:
                handVerify[letra] -= 1
            else:
                return False
    else:
        return False
    
    return True





# XXXXXXXXX Default Config XXXXXXXXX
wordList = loadWords()

hand = {'a':1, 'q':1, 'b':2, 'y':2, 'e':1, 'i':1}
word = 'abbey'

# # XXXXXXXXX Output XXXXXXXXX

print(isValidWord(word, hand, wordList))