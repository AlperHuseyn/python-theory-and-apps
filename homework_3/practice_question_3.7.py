""" My approach to practice question #3.7 """

text = input('Enter a text: ')

words = text.split()[::-1]
for word in words:
    if words.count(word) != 1:
        words.remove(word)


print(words[::-1])