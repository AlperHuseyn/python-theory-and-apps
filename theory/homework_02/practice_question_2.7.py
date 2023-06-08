""" My approach to practice question #2.7 """

text = input('Please enter a text: ')

counts = {}
for char in set(text):
    counts[char] = text.count(char)

print(counts)
