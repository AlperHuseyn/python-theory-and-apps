""" Instructor solution(s) for practice question #2.7 """

# 1st way: Easier
s = input('Please enter a text: ')

d = {}
for ch in s:
    d[ch] = s.count(ch)

print(d)

# 2nd way: Harder solution
s = input('Please enter a text: ')

d = {}
for ch in s:
    d[ch] = d[ch] + 1 if ch in d else 1

print(d)
