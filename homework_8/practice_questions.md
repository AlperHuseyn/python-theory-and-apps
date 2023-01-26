1. Write the Array class as follows:

- The Array class should create an instance attribute called array and store elements in it. The `__init__` method's parameter 
structure is as follows:

```python
def __init__(self, *args):
    pass
```
- The Array class's `add` method adds a new element to the object's array instance attribute. The method's parameter 
structure is as follows:

```python
def add(self, val):
    pass
```

The method should add the values taken by the arguments to the class's list type array instance attribute. For example:

`a = Array(1, 2, 3, 4, 5)`

As a result of this operation, the `a` object's array instance attribute will have the values `1, 2, 3, 4, 5`. The method 
can also take a list as an argument. In this case, the elements of the list should also be added to the array instance 
attribute, not the list itself. For example:

`a = Array(1, 2, [3, 4, 5], 6, [7, 8])`

As a result of this operation, the object's array instance attribute should have the values `1, 2, 3, 4, 5, 6, 7, 8`.
However, nested lists cannot be an argument. 

- The Array class's `__repr__` method prints the values in the array instance attribute to the screen with `,` between them. 
The method's parameter structure is as follows:

```python
def __repr__(self):
    pass
```

The class will have the following elements:

```python
class Array:
    def __init__(self, *args):
        pass

    def __repr__(self):
        pass

    def add(self, val):
        pass
```

You can test the class with the following code:

```python
a = Array(1, 2, [3, 4, 5], 6, [7, 8])

a.__repr__()
a.add('ali')
a.__repr__()
```
As a result, the following output should be seen on the screen:
```
1, 2, 3, 4, 5, 6, 7, 8, Ali
```
---

2. Write the Date class as follows:

- The class's `__init__` method will take in `day, month`, and `year` information and store them in instance attributes 
named `day, month`, and `year`. The method should also create an instance attribute named `tdays`, which stores the number of 
days that have passed since `01/01/1900`. (You should use the _total_days method, you will write, for this.) The parameter 
structure of the init method will be as follows: 

```python
def __init__(self, day, month=None, year=None):
    pass
```

If a method is given only one argument, and it is of type int, this value will represent the number of days passed since 
`01/01/1900` and this value will be converted into date information and placed in the object's `day, month, year` 
instance attributes. If the method is given only one argument, and it is of type str, in this case, the text should be 
in the format `dd/mm/yyyy`. This text should be parsed and again placed in the object's `day, month, year`, and `tdays` 
instance attributes. That is, an object of the Date type can be created with one of the following three formats:

```python
date1 = Date('12/10/2007')
date2 = Date(33760)
date3 = Date(10, 12, 2009)
```

- The `__init__` method should throw an exception for inappropriate parameter inputs. Use the following statement to 
throw an exception:

```python
raise ValueError('invalid argument')
```

- The method named `__repr__` of the class should print the date in the format `dd/mm/yyyy-day` inside the specified object 
using the self parameter. The parameter structure of the method is as follows:

```python
def __repr__(self):
    pass
```

- The method named `_total_days` of the class should return the number of days passed from `01/01/1900` using the 
instance attributes `day, month`, and `year` with the self parameter. The parameter structure of the method is as 
follows:

```python
def _total_days(self):
    pass
```

When writing this method, the datetime module from the Python standard library should not be used.

(This method will also place the number of days passed since `01/01/1900` in the `tdays` instance attribute, when called 
from within the `__init__` method.) To find the number of days passed since `01/01/1900`, it is necessary to know if a 
year is a leap year. Years that are divisible by 4 but not divisible by 100 are leap years. Additionally, if a year is 
divisible by 400, it is also a leap year.

```python
@staticmethod
def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year %400 == 0
```

- The method named `_convert_date` in the class should do the opposite of what the `_total_days` method does. That is, 
this method should take as a parameter the number of days that have passed since `01/01/1900` and place  it should return 
the date represented by that number of days in the form of a `triplet (day, month, year)`.

```python
def _convert_date(self, tdays):
    pass
```

- The method named `get_day_text` in the class should return a text indicating which day of the week the date specified 
by the object's instance attributes corresponds to. The method's parameter structure is as follows:

```python
def get_day_text(self):
    pass
```

- The `comparison operator methods` of the class should be written to compare two Date objects in the following format:

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

These methods can be written using the number of days passed since `01/01/1900` of both dates.

- The class's `__add__` method should add a day to a date and return the result as a Date object. Make sure to allow for the 
operands to be reversed in this operator method. Similarly, the `__sub__` method should subtract a day from a date and 
return the result as a Date object. Additionally, the sub method should also be able to subtract two dates and return the 
result as the number of days between them as an `int`.

This can actually be written by adding this day value to the number of days passed from `01/01/1900` and performing the 
reverse transformation.

The basic methods of the class should be as follows:T

```python
class Date:
    def __init__(self, day, month=None, year=None):
        pass

    def __repr__(self):
        pass

    def _total_days(self):
        pass
    
    def _convert_date(self, tdays):
        pass
        
    def get_day_text(self):
        pass

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

    def __add__(self, days):
        pass

    def __sub__(self, days):
        pass
```
In addition to the methods above, you can also add other methods to the class to make your work easier.

You can test the class with the following code:

```python
d = Date(37320)
k = Date('12/11/1992')
m = Date(10, 12, 2022)

print(d)
print(k)
print(m)

result = m + 2
print(result)

result = k - 2
print(result)

if k > m:
    print('k > m')
elif k < m:
    print('k < m')
elif k == m:
    print('k == m')
```


