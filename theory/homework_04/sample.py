import homework

# Testing practice question 4.1
a = [1, 2, 2, 5, 3, 6, 6, 7, 3, 8, 9, 2, 1, 4, 4]
b = homework.exclude_repeated_items(a)
print(b)

print('#####################################')

# Testing practice question 4.2
homework.disp_pascal_triangle(5)

print('#####################################')

# Testing practice question 4.3
homework.diamond_pattern(5)
print('##')
homework.diamond_ins(5)

print('#####################################')

a = [(1, 3), (3, 6), (6, 9), (9, 1)]
print('Domino' if homework.is_domino(a) else 'Not a Domino')
print('##')
a = [(1, 3), (3, 6), (6, 9), (9, 1)]
print('Domino' if homework.is_domino_ins(a) else 'Not a Domino')

print('#####################################')
