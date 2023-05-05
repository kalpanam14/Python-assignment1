value = input('Enter the word or name: ')

rev = ''
for i in value:
    rev = i + rev

print('The reversed string is:',rev)