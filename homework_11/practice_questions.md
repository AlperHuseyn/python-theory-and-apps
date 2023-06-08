---

1. Write an iterable class named `GrepIterable` that gives the lines in which certain words appear in a file. The class's 
`__init__` method will take the path of the file and the text to be searched for.

```python
def __init__(self, path, text):
    pass
```

The next method of the iterator object will give the line as follows:

`<line number>: characters in the line`

For example:

```
'<10>: today the weather is very nice'
'<12>: the weather is starting to warm up'
...
```

An example of the use of the class can be given as:

```python
for line in GrepIterable('test.txt', 'ankara'):
    print(line)
```

---

2. Write a class named `LastLinesIterable` that returns the last n lines of a file from the end to the beginning. The 
class's `__init__` method should take the file path and the number of lines to be returned as parameters. The class should 
return one line per iteration:

```python
def __init__(self, path, n):
    pass
```

An example usage could be:

```python
for line in LastLinesIterable('test.txt', 10):
    print(line)
```

---

3. Write a class named `CSVReaderIterable` that performs the same function as the `read_csv function` from the previous 
assignment, which reads CSV-like files. The class should return a row from the CSV-like file in list format on each iteration. 
The parameter structure for the class's `__init__` method is as follows:

```python
class CSVReaderIterable:
    def init(path, sep=',', skiprows=0, converter={}):
        pass
...
```

- The first parameter of the method specifies the path of the file. 
- The second parameter specifies the column separator characters. This parameter can be a string. The characters in the 
string individually specify the separator characters. (For example, sep=', ' means that both the space and the comma are 
separators. However, in many CSV readers, this sep parameter means "a comma followed by a space is the whole separator". 
But in our function, sep=', ' means that both the space character and the comma character are independent separators.) 
The third parameter specifies how many rows at the beginning of the file will be ignored during processing. (For example, 
the first rows of CSV files may contain a header. To skip this, skiprows=1 can be done.) 
- The last parameter specifies which columns will be converted to which type and placed in the final matrix. This parameter 
is of the dictionary type. The key of the dictionary is the column number and the value is the function that performs the 
conversion. For example:

`converter = {1: int, 2: float, 3: myconverter}`

The parameter of the conversion functions must be of type str and the return value should be the value to be placed in the 
final matrix.

Please note that quoted fields should be treated as a single element during parsing. For example, if the CSV file is like this:

```
Name, Phone Numbers, Options
Ali Serce,"05325678796,02162658765","1,2,3"
Sacit Apaydin,"05325456879,02123658755","5,8,9"
...
```

The quoted fields in the rows of this file will be treated as single elements.

---
