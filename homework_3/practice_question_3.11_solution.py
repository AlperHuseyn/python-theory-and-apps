""" Instructor solution(s) for practice question #3.11 """
# This sorting algorithms are not necessary, sort() and sorted() can be used and these are better solutions
# sorted() uses quicksort sorting algorithm


# 1st way: using bubble sort
def sort_tuple_list(tuple_list):
    for i in range(len(tuple_list) - 1):
        for k in range(len(tuple_list) - 1 - i):
            if tuple_list[k] > tuple_list[k + 1]:
                tuple_list[k], tuple_list[k + 1] = tuple_list[k + 1], tuple_list[k]


a = [('Tom', 19, 80), ('Json', 22, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json',21, 85)]
sort_tuple_list(a)
print(a)


#2nd way: using selection sort
def sort_tuple_list(tuple_list):
    for i in range(len(tuple_list) - 1):
        minval = tuple_list[i]
        minval_idx = i
        for k in range(i + 1, len(tuple_list)):
            if tuple_list[k] < minval:
                minval = tuple_list[k]
                minval_idx = k

        tuple_list[minval_idx], tuple_list[i] = tuple_list[i], tuple_list[minval_idx]


a = [('Tom', 19, 80), ('Json', 22, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json',21, 85)]
sort_tuple_list(a)
print(a)
