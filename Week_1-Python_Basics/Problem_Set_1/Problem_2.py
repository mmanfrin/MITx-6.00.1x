# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2


s = 'azcbobobegghakl'

count = 0

for i in range(0,len(s)):
    if s[i:i+3] == 'bob':
        count += 1
        bob = s[i:i+3] + str(count)

print('Number of times bob occurs is: ', count)