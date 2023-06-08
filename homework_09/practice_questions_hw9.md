1. Write the class named Time as specified below:

- In the `__init__` method of the class, the time information that the object will hold is obtained and stored in instance 
attributes `hour, minute, second`. Additionally, this time information will be converted to the number of seconds 
passed from `00:00:00` and this will be stored in the instance attribute `t_seconds` of the class.

```python
def __init__(self, hour=0, minute=0, second=0):
    pass
```
You should use the `_total_seconds` method, which will be explained later, to place the value of the `t_seconds` attribute.

- The class's `__str__` method will give the time as a string in the `hh:mm:ss` format.

```python
def __str__(self):
    pass
```

- The `__repr__` method of the class will return the time in the str format `hh:mm:ss-(number of seconds passed from 0)`.

```python
def __repr__(self):
    pass
```

- The method named `_total_seconds` of the class will convert the time value stored in the instance attributes; `self.hour, 
self.minute`, and `self.second` from `00:00:00` to the number of seconds passed and will return this value.

```python
def _total_seconds(self):
    pass
```

Of course, the instance attribute named `t_seconds` of the class should actually be calculated using this method. 

- Add a method named `_seconds_to_time` that converts the class. This method should take the total number of seconds 
passed from `00:00:00` as a parameter and perform the reverse conversion by placing the time in the instance attributes
`self.hour, self.minute, self.second,` and `self.t_seconds` of the class.

```python
def _seconds_to_time(self, seconds):
    pass
```

- Add the following operator methods that compare two time values in the class:

```python
def __lt__(self, t):
    pass

def __le__(self, t):
    pass

def __gt__(self, t):
    pass

def __ge__(self, t):
    pass

def __eq__(self, t):
    pass

def __ne__(self, t):
    pass
```

All of these methods will return a Boolean value.

- Add to the class operator methods that add two Time objects and a Time object with an int object. If the other operand 
is `int` it should be interpreted as the number of seconds. This method should return a new `Time object`.

```python
def __add__(self, t):
    pass
```

The second parameter of the method can be of the type `Time` or `int`. The value obtained should give the time of the 
next day if it exceeds `23:59:59`. Also, add a `__radd__` method to the class, which can add a right operand `Time` to 
the left operand `int`:

```python
def __radd__(self, t):
    pass
```

- Add to the class a `__sub__` operator method that subtracts two `Time` objects and one `Time` object from an `int`object. 
If the other operand is `int` it should be interpreted as the number of seconds. This method should return a `Time` object as the return value.

```python
def __sub__(self, t):
    pass
```

- Also, add a `__rsub__` method to the class, which can subtract the right operand Time from the left operand int:

```python
def __rsub__(self, t):
    pass
```

If the total number of seconds obtained from these operations is negative, the wrapping should be done from above (i.e. ,
subtracting one second from `00:00:00` should give `23:59:59` time).

- Write a `__int__` method for the class. This method should return the number of seconds that have passed since 00:00:00.

```python
def __int__(self):
    pass
```

Please note that this value is already stored in the `t_seconds` instance attribute of the class.

- Write a `__bool__` method for the class. If the time within the `Time` object is `0` this method should return `False`, 
otherwise it should return `True`.

- Write `__getitem__` and `__setitem__` operator methods for the class. These methods should take an index parameter. 
This index can be `0, 1, 2 (0 = Hour, 1 = Minute, 2 = Second)`. They should be used to get and set the relevant component 
of the time. In `setitem` when you set a component of the time, do not forget to update the `t_seconds` value in the object's 
instance attribute.

You can test the class with the following code:

```python
t1 = Time(22, 10, 24)
result = t1 + 5700
print(result)

t2 = Time(5, 40, 34)
result = t1 + t2
print(result)

result = t1 - t2
print(result)

if t1 > t2:
    print('t1 > t2')
elif t1 < t2:
    print('t1 < t2')
elif t1 == t2:
    print('t1 == t2')

result = int(t1)
print(t1)

print('Time non-zero' if t1 else 'Time zero')

t1[0] = 23
print(t1)
```

---


