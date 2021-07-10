def search4vowels():
    """Print vowels which was found in input word."""
    vowels = set('aeiou')
    word = input('Write a word to search for vowels:')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

search4vowels()

