""" My approach to practice question # 6.1 """

text = 'today the weather is very nice'
vocals = {vocal for vocal in text if vocal in ['a', 'e', 'i', 'o', 'u']}
print(vocals)