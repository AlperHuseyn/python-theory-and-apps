""" My approach to practice question #6.6 """

s = 'today the weather is very beautiful'

result = ''
for idx, word in enumerate(s.split()):
    temp = '' if idx == 0 else ' '
    for ch in word:
        if ch not in 'aeiou':
            temp += ch
    result += temp
print(result)
