from ps4a import *

loadWords()
print()

hand = {'a':1, 'q':1, 'b':2, 'y':2, 'e':1, 'i':1}
word = 'abbeya'

# # copiando dicionatio (hand)
# handVerify = hand.copy()

# # loop busca/del
# for letra in word:
#     # checa se existe letra no dicionario
#     if letra in handVerify and handVerify[letra] > 0:
#         handVerify[letra] -= 1
#     else:
#         print('False')
#         break
# print('True')

# # print(handVerify)

# x = list(hand.values())