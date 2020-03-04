from ps4a import *

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    # params
    choice = ''
    n = HAND_SIZE
    hand = {}
    # main loop
    while choice != 'e':
        # input do jogo
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        # se N - novo jogo
        if choice == 'n':
            # chama novo jogo
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, n)
        
        # se R - replay jogo
        elif choice == 'r':
            # chama mao anterior
            if hand == {}:
                print('\nYou have not played a hand yet. Please play a new hand first!\n')
            else:
                playHand(hand, wordList, n)
            
        # se E - termina jogo
        elif choice == 'e':
            # termina o jogo
            # print('\nGame Over!\n')
            break
        # senão - comando invalido
        else:
            print('\nInvalid command.\n')
    return

wordList = loadWords()
HAND_SIZE = 7
n = HAND_SIZE

playGame(wordList)

