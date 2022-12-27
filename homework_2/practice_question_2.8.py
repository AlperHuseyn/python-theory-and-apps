""" My approach to practice question #2.8 """

lst = [12, 56, 89, 32, 19, 99, 43]
s_lst = [0] * len(lst)

for idx in range(len(lst)):
    flag = True
    for digit in str(lst[idx])[::-1]:
        s_lst[idx] += (int(digit) * 10 if flag else int(digit))
        flag = False

print(lst)
print(s_lst)
