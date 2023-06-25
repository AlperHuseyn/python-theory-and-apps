## 1) Performance Graph for Bubble Sort Algorithm

Please draw a performance graph for bubble sort algorithm based on input size. The algorithm is given below:

```python
def bsort(a):
    for i in range(len(a)-1):
        for k in range(len(a)-1-i):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
```

Explanation:
    
* You can use the `time function` from the `time module` to measure the runtime between two points. For example:

```python
t1 = time.time()
...
t2 = time.time()
```

* A total of 20 experiments will be conducted. In the first experiment, 1000 randomly generated elements will be sorted using the `bsort` function. In each subsequent experiment, the number of elements will be increased by 1000. This way, you will have timing data for randomly generated lists of elements ranging from 1000 to 20000.

* Generate random numbers between 0 and 1_000_000 (one million). You can use the `sample function` from the `random module` like this:

```python
x = random.sample(range(1000000), n)
```

Alternatively, you can use the `randrange` or `randint` functions from the `random module` with the following command:

After these operations, you should have two lists x and y. The x list should contain 20 values ranging from 1000 to 20000, and the y list should contain the corresponding runtimes.

You can plot the graph as follows:

import matplotlib.pyplot as plt


```python
plt.plot(x, y)
plt.show()
```

## 2)Print Calendar of a Given Month and Year

Write a function called `prmonth` that prints the calendar of a given month and year to the screen.

```python
def prmonth(year, month):
    pass
```

The first parameter of the function specifies the year, and the second parameter specifies the month. The calendar will be printed to the screen in the following format:

    ```
        August 2018
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31
    ```



