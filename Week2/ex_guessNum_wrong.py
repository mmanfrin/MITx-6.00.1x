# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 83?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
# Game over. Your secret number was: 83

low = -1
high = 101
ans = int((high + low) / 2)

print('Please think of a number between 0 and 100!')
print('Is your number 50?')
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

while guess != 'c':
    if guess == 'l':
        high = ans
        ans = int((high + low) / 2)
        print('Is your number ' + str(ans) + '?')
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    else:
        low = ans
        ans = int((high + low) / 2)
        print('Is your number ' + str(ans) + '?')
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        
print('Game over. Your secret number was: ' + str(int(ans)))

# Resposta do site
# print("Please think of a number between 0 and 100!")

# # At the start the highest the number could be is 100 and the lowest is 0.
# hi = 100
# lo = 0
# guessed = False

# # Loop until we guess it correctly
# while not guessed:
#     # Bisection search: guess the midpoint between our current high and low guesses
#     guess = (hi + lo)//2
#     print("Is your secret number " + str(guess)+ "?")
#     user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

#     if user_inp == 'c':
#         # We got it right!
#         guessed = True
#     elif user_inp == 'h':
#         # Guess was too high. So make the current guess the highest possible guess.
#         hi = guess
#     elif user_inp == 'l':
#         # Guess was too low. So make the current guess the lowest possible guess.
#         lo = guess
#     else:
#         print("Sorry, I did not understand your input.")

# print('Game over. Your secret number was: ' + str(guess))