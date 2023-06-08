----

1. Check if given two lists are palindrome. If yes, print 'True', 'False' otherwise.

Explanation:

For the below lists, output must be `True`.

```python
l1 = [10, 'ali', 'veli', 20, 'selami']
l2 = ['selami', 20, 'veli', 'ali', 10]
```
----

2. First create a list. Then swap first half of this list elements with the second half of it. Print the output to the
console.

Explanation:

Assume there is a list such as ```l3```.

```python
l3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
```

After the swap process `l3` must be look like this:
```
output: [60, 70, 80, 90, 100, 10, 20, 30, 40, 50]
```
Hint: List can have an odd number of elements. If this is the case, middle element must remain at the same index after
the swap.
```python
l4 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

output: [60, 70, 80, 90, 50, 10, 20, 30, 40])
```
----

3. Request single digit type int number from the stdin. (Let n represent the entered number) Print below computation to
the stdout.

```n + nn + nnn + nnnn```

----

4. Request 3 digits numerical text of type int from the stdin. Convert this text to int then print it to the console
without using int(...) function.

Explanation:

Assume '123' is given. This can be gotten as ```1 * 100 + 2 * 10 + 3 * 1```.

Hint: ord(...) built-in function can be used.

----

5. Request a text and a number from the stdin. Without using the center method of the str class, center the entered
text with spaces in the area equal to the entered number. (So here, it is requested that write a code what is doing
the same as center method of the str class) Centered text must be of type str and printed to the stdout.

Explanation:

In case of not equality on the both sides of space chars, left side must have one space more than right side.
You can test the number of space chars printing colons like below:

```python
print(':' + s + ':') or print(':', s, ':', sep='')
```
----


