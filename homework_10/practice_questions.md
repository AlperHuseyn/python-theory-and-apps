--- 

1. Write a function called `mygrep` that prints lines containing certain words in a file in the following format:

```python
def mygrep(path, text):
    pass
```
Output:

`<line number>: characters in the line`

For example:

```python
mygrep('test.txt', 'weather')
```

Output should be similar to this:

```
<10>: today's weather is very nice
<12>: the weather is getting warmer
...
```

---

2. Write a function named `disp_last_lines` that prints the last n lines of a file to the screen. 

```python
def disp_last_lines(path, n):
    pass
```

The first parameter of the function specifies the path of the file, and the second parameter specifies the number of lines.

---

3. Write a function named `get_count` that returns the values for `the number of lines, words,` and `characters` in a file 
as a triplet:

```python
def get_count(path):
    pass
```

The function will return in the form of a `tuple (line, word, character)`. The `\n` characters, which represent line 
breaks in text files, should also be counted as a character. For example:

`lcount, wcount, ccount = get_count('test.txt')`

---

4. Write a function called `get_file_size` that uses the `seek` and `tell` methods of a file object to obtain the length 
of a file and return the value in the form of a return value:

```python
def get_file_size(path):
    pass
```

---

5. Write a function called `copy_file` that copies a file by reading `n bytes` from the source file in a loop and writing 
them to another file:

```python
def copy_file(source_path, dest_path):
    pass
```

Don't forget to open the file in binary mode.

---

6. Please write a function named `read_csv` that reads from a file similar to a CSV file and returns the information in 
a matrix format (a list of lists) and that will not separate the fields in double quotes. The function's parameter 
structure is as follows:

```python
def read_csv(path, sep=',', skiprows=0, converter={}):
    pass
```

- The first parameter of the function specifies the path of the file. 
- The second parameter specifies the column separator characters. This parameter can be a string. The characters in the 
string specify the separator characters individually. (For example, sep=', ' in which case the separator is both a space 
and a comma. However, in this sep parameter, in many CSV readers, "a comma after a space" means that the entire comma is 
a separator. However, in our function, sep=', ' specifies that both the space character and the comma character are 
independent separators.) 
- The third parameter specifies how many rows from the beginning of the file will not be taken into account when 
processing. (For example, the first rows of CSV files may have a header section. This can be skipped by skiprows=1.) 
- The last parameter specifies which column will be converted to which type and placed in the final matrix. This parameter 
is a dictionary type. The dictionary's key is the column number and the value is the conversion function. For example:

`converter = {1: int, 2: float, 3: myconverter}`

The parameter of the conversion functions must be of the str type and the return value must be the value to be placed 
in the final matrix.

Please note that double-quoted fields will be considered as a single element. For example, consider the following CSV file:

```
Name Surname,Phone Numbers, Options
John Wick,"05325678796,02162658765","1,2,3"
Angelo Merkel,"05325456879,02123658755","5,8,9"
...
```

In this file, the double-quoted fields will be considered as single elements.

---



