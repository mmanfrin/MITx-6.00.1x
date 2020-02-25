def score(word, f):
    import string
    scorelist=[]
    index=0
    word = word.casefold()
    for char in word:
        alphabet_location=string.ascii_lowercase.find(char)+1
        # index=index
        scorelist.extend([alphabet_location*index])
        index += 1
    max_score=max(scorelist)
    scorelist.remove(max_score)
    second_max=max(scorelist)
    return f(max_score,second_max)
    
def f(x1,x2):
    return x1+x2

print(score('adD',f))