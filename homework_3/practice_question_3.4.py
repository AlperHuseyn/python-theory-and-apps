""" My approach to practice question #3.4 """


def is_armstrong(num):
    pw = len(str(num))
    pow_sum_digits = 0
    temp = num
    for _ in range(pw):
        pow_sum_digits += (temp % 10) ** pw
        temp //= 10

    if pow_sum_digits == num:
        return True
    else:
        return False


while True:
    val = int(input('Enter a value: '))
    if val == 0:
        break
    print('Armstrong' if is_armstrong(val) else 'Not Armstrong')


def print_armstrongs(n):
    for i in range(1, n + 1):
        if is_armstrong(i):
            print(i, end=' ')
        else:
            continue


print_armstrongs(1_000_000)
