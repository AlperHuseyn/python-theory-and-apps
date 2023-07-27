# Create an SQLite3 database that holds students' basic information and their grades from various courses as described below, and perform the specified operations on this database.

Descriptions:

- The name of the database should be `"student_notes.sqlite."`

- The database will consist of three tables. The tables and their properties are described below:

```
student Table:

student_no: Student number. Type: INTEGER. To be taken as the Primary key.
student_name: Student's name. Type: VARCHAR(64) or directly TEXT.
student_photo: Student's photo. Type: BLOB.

class Table:

class_id: Type: Integer. To be taken as Primary key and autoincrement. It will act as a foreign key for the grade table.
class_name: Type: VARCHAR(32) or directly TEXT. Represents the name of the course.
class_week_hours: The weekly class hours of the course.

grade Table:

student_no: Student number. Indicates which student the grade belongs to. To be taken as Primary key and autoincrement. Type: INTEGER.
class_id: Indicates which course the grade belongs to. Type: INTEGER.
class_exam_no: The number of the exam (1 for the first exam, 2 for the second, etc.). Type: INTEGER.
class_grade: Represents the grade obtained in the respective course out of 100. Type: INTEGER.
```

- Create the database tables using the `"CREATE TABLE IF NOT EXISTS"` SQL commands within the program.

- Create a menu as follows inside a loop:

1) Course Entry
2) Student Entry
3) Grade Entry
4) Student Query
5) Exit

Your selection:

* When `"Course Entry"` is selected, the following input should be taken:

`Enter the course name and weekly class hours:`

An example input should be as follows:

`Physics, 6`

Note the input is separated by a comma. Here, the course name is "Physics" and the weekly class hours are "6."

* When `"Student Entry"` is selected, the following inputs should be taken in order:

`Enter the student's full name, student number, and the file path of the student's photo:`

An example input could be:

`Ali Serçe, 1234, ali_serce.jpg`

Note that the information is separated by commas.

While adding the student to the database, use the execute method with parameters. The field corresponding to the photo, which is BLOB, must be a bytes object. You can obtain the bytes object for the photo data as follows:

```python
with open(path, 'rb') as f:
    b = f.read()
```

Alternatively, you can perform this operation as follows:

```python
f = open(path, 'rb')
b = f.read()
f.close()
```

Make sure to open the file in `"binary mode."`

* When `"Grade Entry"` is selected, the system should ask for which student's grade in which course will be entered:

`Enter the student no, the course name, exam number, and grade:`

An example input would be:

`820, Physics, 1, 70`

Here, the input consists of the student's full name, followed by the course name, then the exam number, and finally the grade. Make sure to separate them with commas.

* When `"Student Query"` is selected, the following input should be asked:

`Enter the student's number:`

If the user presses the `ENTER` key without entering a number, the information of all students will be listed. If a student number is entered, only the information of the student with that number will be displayed. The listing should be as follows:

```
Name: Kaan Aslan
Number: 1634

Physics: 60, 70, 30
Mathematics: 40, 70
Literature: 80, 60, 90

Photo

Weighted Average Grade: 75
```

To display the photo, we first need to obtain the image data as a bytes object. Then you can display it as shown below:

```python
import PIL
import IPython
import io

bio = io.BytesIO(b)
image = PIL.Image.open(bio)
image.thumbnail((200, 300))
IPython.display.display(image)
```

Here, "b" represents the bytes content of the photo obtained from the SELECT result. The thumbnail method resizes the image while preserving the aspect ratio. You can modify the values here.

The weighted average grade should be calculated as follows: Calculate the average of the grades obtained by the student in each course. Then, multiply this average by the weekly class hours of that course, sum all of these results, and finally divide by the total weekly class hours of all courses the student takes. For example, let's assume the weekly class hours are 6 for Physics, 6 for Mathematics, and 3 for Literature. In this case, the weighted average grade for the student mentioned above should be calculated as follows:

```((60 + 70 + 30) / 3 * 6 + (40 + 70) / 2 * 6 + (80 + 60 + 90) / 3 * 3) / 15```
