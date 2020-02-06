# Exercise: while exercise 3

# (5/5 points)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# 3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we
# define end to be 6, your code should print out the result:

# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

# For problems such as these, do not include input statements or define variables we will provide for you. Our automating testing will
# provide values so write your code in the following box assuming these variables are already defined.

end = 6

soma = 0
for i in range(0, end + 1):
    soma += i
print(soma)

print(total)