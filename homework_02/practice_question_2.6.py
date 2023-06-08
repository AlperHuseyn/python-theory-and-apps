""" My approach to the practice question #2.6 """

text = input('Please enter a text: ')

upper_count = 0
lower_count = 0
for char in text:
    if not char.isalpha():
        continue
    if char.isupper():
        upper_count += 1
    else:
        lower_count += 1

print(f'upper_count: {upper_count}, lower_count: {lower_count}')
