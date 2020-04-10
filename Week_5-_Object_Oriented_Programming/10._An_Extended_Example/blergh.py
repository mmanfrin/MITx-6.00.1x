import string

# k = int(input('entre a key: '))
k = 250
# enc = int((k/26)+1)
# alph = str(string.ascii_lowercase) * enc
dic = str(string.ascii_lowercase) * int((k/26)+1)
print(len(alph))