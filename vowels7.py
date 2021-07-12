vowels = set('aeiou')
word = input('Write a word to search the vowels:')
found = vowels.intersection(set(word))
print(found)


