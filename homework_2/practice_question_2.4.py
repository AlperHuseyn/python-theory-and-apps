""" My approach to the practice question #2.4 """

import string

text = input('Please enter a text: ')

words = []
current_word = ''

for char in text:
    if char in string.whitespace + string.punctuation:
        current_word = ''
        continue
    else:
        current_word += char

# To get the last word
if current_word:
    words.append(current_word)


print(words)
