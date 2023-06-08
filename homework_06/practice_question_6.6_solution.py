""" Instructor solution(s) for practice question #6.6 """

s = 'today the weather is very beautiful'

result = ''.join([ch for ch in s if ch not in 'aeiou'])
print(result)
