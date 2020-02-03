#checa primeiro caso de bob
#    a partir dessa posicao, checa outro caso de bob
#        ...

s = 'azcbobobeghgffyboboboboghakl'
count = 0
l = len(s)

for i in range(0, l):
    pos = s.find('bob',i)
    count += 1

print(count)