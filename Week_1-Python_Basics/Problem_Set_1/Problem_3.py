s = 'azcbobobegghakl'
# s = 'qljjdyxliz'
# s = 'zyxwvutsrqponmlkjihgfedcba'
# s = 'eazwzdugel'
# s = 'ykuwpnijsaajk'

holder = s[0]
seq = ""

for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        holder = holder + s[i]
    else:
        if len(holder) > len(seq):
            seq = holder
        holder = s[i]

if len(holder) > len(seq):
    seq = holder

print('Longest substring in alphabetical order is: ', seq)