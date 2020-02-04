# cube = int(input('Enter an integer :'))
cube = 8
scroot = input('Square or Cube Root? ')

if scroot == 'square': 
    for guess in range(cube+1):
        if guess**2 == cube:
            print('Cube root of', cube,'is', guess)
elif scroot == 'cube':
    for guess in range(cube+1):
        if guess**3 == cube:
            print('Cube root of', cube,'is', guess)
else:
    print('Denied')