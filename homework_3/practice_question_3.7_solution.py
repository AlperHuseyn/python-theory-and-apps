""" Instructor solution for practice question #3.7 """

text = input('Enter a text: ')

words= []
for word in text.split():
    if word not in words:
        words.append(word)


print(words)