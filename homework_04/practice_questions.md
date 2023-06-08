---
In the following questions, create all the functions requested in a file called homework.py. Then import this file
from a file called sample.py and test the functions. If you will also be doing the test procedures in the homework.py
file, make sure that these codes are not run when importing.

---

1. Please write the following function that removes repeating elements from a list and creates a new list from the
remaining non-repeating elements:


    def exclude_repeated_items(a):
        pass

An example usage could be:

    import homework
    
    a = [1, 2, 2, 5, 3, 6, 6, 7, 3, 8, 9, 2, 1, 4, 4]
    b = homework.exclude_repeated_items(a)
    print(b)

Here, the following list should be printed:

    [1, 2, 5, 3, 6, 7, 8, 9, 4]

Note that the relative order of the elements has not changed.

---

2. Write the following function that prints a Pascal triangle:


    def disp_pascal_triangle(n):
        pass

The parameter of the function is the height of the Pascal triangle. For example, if the value of n is 5:

        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1

Remember that the elements of the Pascal triangle are the number of k-subsets of an n-element set. The rows give the 
number of elements in the set, and the elements in the rows give the number of subsets (starting from 0) of that set. 
The combination C(n, k) is in the form n! / (k ! * (n – k)!), where "!" denotes the factorial function.

---

3. Write a function that draws the pattern described below with the given number from the keyboard:


    size-3
    ----c----
    --c-b-c--
    c-b-a-b-c
    --c-b-c--
    ----c----
    
    size-5
    --------e--------
    ------e-d-e------
    ----e-d-c-d-e----
    --e-d-c-b-c-d-e--
    e-d-c-b-a-b-c-d-e
    --e-d-c-b-c-d-e--
    ----e-d-c-d-e----
    ------d-e-d------
    --------e--------

---

4. Write the is_domino function that checks if the tuples in a list of two-element tuples are dominos.


    def is_domino(l):

The function returns a boolean value. In domino tuples, the second element of the tuple is the same as the first
element of the next tuple. For example, the following tuple list is a domino:

    [(1, 3), (3, 6), (6, 9), (9, 1)]

---
