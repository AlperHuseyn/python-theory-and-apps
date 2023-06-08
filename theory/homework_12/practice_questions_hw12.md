1. The count function in the itertools module of the Python standard library gives us an iteration (iterator) object. 
When this object is iterated over, values are obtained starting from a certain value and increasing indefinitely with 
increments. Its parametric form is as follows:

```python
def count(start=0, step=1):
    pass
```

The standard library's ```count``` is written in a class format that can be iterated over. However, you can also write 
this function in both a class format that can be iterated over and a generator function format. You can test it with the 
following code:

```python
iterator = itertools.mycount(10, 2)

for index, x in enumerate(iterator):
    if index == 10:
        break
    print(x, end=' ')
```

---

2. The standard ```cycle``` function in the itertools module takes an iterable object and gives us an iteration object. 
When this object is iterated over, the elements of the iterable object we gave it are given in a cyclical manner 
indefinitely. Write this function in both a class format that can be iterated over and a generator function format. You 
can test it with the following code:

```python
import itertools

iterator = mycycle('ABC')

for index, c in enumerate(iterator):
    print(c, end=' ')
    if index == 30:
        break
```
---

3. The itertools module also has an interesting function called ```islice```. The parameteric structure of the function is as follows:

```python
def islice(iterable, start, stop=None, step=1)
    pass
```

The ```start, stop, step``` parameters of the function are consistent with the semantics of the range function. The function 
gives us an iteration object. We can get the first n elements of that iteration object. This function is very practical because 
if someone gives us an iterable object, and we want to work on a certain amount of elements of it, we need such a function. 
Generally, the ```islice``` function is used in combination with other functions. Write the ```islice``` function in both a 
class format that can be iterated over and a generator function format. You can test it with the following example:

```python
import itertools

for c in myislice(itertools.cycle('ABC'), 20):
    print(c, end=' ')
```

Of course, if the iterable object given to us ends prematurely, the function should also end the operation.

---

4. The ```repeat``` function in the itertools module has the following parametric structure:

The function gives us an iterator object. When this object is iterated over, a specified number (times parameter) of the 
value we provided is obtained. For example:

```python
import itertools

for x in itertools.repeat(10, 5):
    print(x, end=' ')
```

If the second parameter (times parameter) is ```not given``` or ```None``` is passed, this value is given indefinitely. Write this function in both an iterable class format and a generator function format.

---
