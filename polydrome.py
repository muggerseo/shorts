string = input('type word to a check for polydrome: ')

if (string==string[::-1]):
    print("It's a polydorome!")
else:
    print("It's not a polydrome!")