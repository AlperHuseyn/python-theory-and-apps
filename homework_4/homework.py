import math


# Practice question 4.1, my approach
def exclude_repeated_items(lst):
    nlst = lst[::-1]
    for elem in nlst:
        elem_count = nlst.count(elem)
        while elem_count != 1:
            nlst.remove(elem)
            elem_count -= 1

    return nlst[::-1]



# Instructor solution for 4.1
def exclude_repeated_items_ins(lst):
    nlst = []
    for elem in lst:
        if elem not in nlst:
            nlst.append(elem)
    return nlst


# Instructor solution to 4.2
def disp_pascal_triangle(n):
    for i in range(n):
        print(' ' * (n - i - 1) * 4, end='')
        for k in range(i + 1):
            print(str(math.comb(i, k)).center(8), end='')
        print()


# Practice question 4.3, my approach
def diamond_pattern(num):
    char = chr(num + ord('a') - 1)
    width = (ord(char) - ord('a') + 1) * 2 - 1
    width += (width - 1)
    tmp = num

    for idx, n in enumerate(range(num, 0, -1)):
        print('-' * (width // 2 - 2 * idx), end='')
        for k in range(num, n - 1, -1):
            print(chr(k + ord('a') - 1), end='')
            print('-' if k != tmp else '', end='')
        tmp -= 1
        for j in range(n + 1, num + 1):
            print('-', end='')
            print(chr(j + ord('a') -  1), end='')
        print('-' * (width // 2 - 2 * idx), end='')
        print()

    for idx, n in enumerate(range(1, num), 1):
        print('-' * (2 * idx), end='')
        for k in range(num, n, - 1):
            print(chr(k + ord('a') - 1), end='')
            print('-', end='')
        for j in range(n + 1, num):
            print(chr(j + ord('a')), end='')
            print('-', end='')
        print('-' * (2 * idx - 1), end='')
        print()


# Practice question 4.3, instructor approach
def diamond_ins(num):
    for i in range(num):
        print('-' * (num - i - 1) * 2, end='')
        index = num - 1
        direction = -1
        for k in range(2 * i + 1):
            if k != 0:
                print('-', end='')
            print(chr(ord('a') + index), end='')
            index += direction
            if k == i - 1:
                direction = 1
        print('-' * (num - i - 1) * 2)

    for i in range(num - 2, -1, -1):
        print('-' * (num - i - 1) * 2, end='')
        index = num - 1
        direction = -1
        for k in range(2 * i + 1):
            if k != 0:
                print('-', end='')
            print(chr(ord('a') + index), end='')
            index += direction
            if k == i - 1:
                direction = 1
        print('-' * (num - i - 1) * 2)


"""
Actually, you can also use a simpler solution by sending an asterisk-delimited argument to the 
print() function and using the sep parameter of the print() function. Here, slicing the relevant 
part of the string.ascii_lowercase string made up of small characters may be difficult. 
To make backward slicing more seamless, you can add a character to the beginning of this string, 
so that the character indexes start from 1.
"""
import string

lowers = 'x' + string.ascii_lowercase
size = int(input('Enter a number: '))
for i in range(size):
    print('-' * (size - i - 1) * 2, end='')
    print(*lowers[size:size - i - 1:-1], sep='-', end='')
    print('-' if i != 0 else '', end='')
    print(*lowers[size - i + 1:size + 1], sep='-', end='')
    print('-' * (size - i - 1) * 2)

for i in range(size - 2, -1, -1):
    print('-' * (size - i - 1) * 2, end='')
    print(*lowers[size:size - i - 1:-1], sep='-', end='')
    print('-' if i != 0 else '', end='')
    print(*lowers[size - i + 1:size + 1], sep='-', end='')
    print('-' * (size - i - 1) * 2)


# Practice question 4.4, my approach
def is_domino(l):
    for i in range(len(l)):
        for _ in range(2):
            return l[i][1] == l[i + 1][0]


# Practice question 4.4, instructor approach
def is_domino_ins(l):
    for i in range(len(l) - 1):
        if l[i][1] != l[i + 1][0]:
            return False
        return True


if __name__ == '__main__':
    print('#####################################')

    # Testing practice question 4.1
    a = [1, 2, 2, 5, 3, 6, 6, 7, 3, 8, 9, 2, 1, 4, 4]
    b = exclude_repeated_items(a)
    print(b)

    print('#####################################')

    # Testing practice question 4.2
    disp_pascal_triangle(5)

    print('#####################################')

    # Testing practice question 4.3
    diamond_pattern(5)
    print('##')
    diamond_ins(5)

    print('#####################################')

    # Testing practice question 4.4
    a = [(1, 3), (3, 6), (6, 9), (9, 1)]
    print('Domino' if is_domino(a) else 'Not a Domino')
    print('##')
    a = [(1, 3), (3, 6), (6, 9), (9, 1)]
    print('Domino' if is_domino_ins(a) else 'Not a Domino')

    print('#####################################')

