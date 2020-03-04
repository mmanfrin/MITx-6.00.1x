# params
    choice = ''
    n = HAND_SIZE
    hand = {}
    player = ''
    # main loop
    while choice != 'e':
        # input do jogo
        choice = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        # se N - novo jogo
        if choice == 'n':
            # chama novo jogo
            hand = dealHand(HAND_SIZE)
            # player vs computer
            while player != 'u' and player != 'c':
                player = input('\nEnter u to have yourself play, c to have the computer play: ')
                # user
                if player == 'u':
                    playHand(hand, wordList, n)
                # computer
                elif player == 'c':
                    compPlayHand(hand, wordList, n)
                else:
                    print('\nInvalid command.\n')
            player = ''
                    
        
        # se R - replay jogo
        elif choice == 'r':
            # chama mao anterior
            if hand == {}:
                print('\nYou have not played a hand yet. Please play a new hand first!\n')
            else:
                # player vs computer
                while player != 'u' and player != 'c':
                    player = input('\nEnter u to have yourself play, c to have the computer play: ')
                    if player == 'u':
                        # user
                        playHand(hand, wordList, n)
                    elif player == 'c':
                        # computer
                        compPlayHand(hand, wordList, n)
                    else:
                        print('\nInvalid command.\n')
                player = ''
                # break
            
        # se E - termina jogo
        elif choice == 'e':
            # termina o jogo
            # print('\nGame Over!\n')
            break
        # senão - comando invalido
        else:
            print('\nInvalid command.\n')
    return