# List/Список

odds = [1, 3, 5, 7, 9, 11]

temps = [32.0, 54.2, 64.3, 63.7]

words = ['hello', 'word']

car_detail = ['Toyota', 'RAV4', 2.2, 60807]

everythings = [temps, words, car_detail]

vowels = ['a', 'e', 'i', 'o', 'u']

# word = input('Provide a word to search for vowels:')
#
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
#
# print(found)

# extract and delete
vowels.pop(3)
print(vowels)

# add lists elements
vowels.extend(['q', 'r', 2])
print(vowels)

# insert element
vowels.insert(3, 'www')
print(vowels)



# Словари
