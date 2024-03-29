from io import BytesIO
from PIL import Image
import os
import sqlite3
import sys


def generate_tables(cursor):
    # Create the necessary tables if they don't exist
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS student(
            student_no INTEGER PRIMARY KEY,
            student_name TEXT(64),
            student_photo BLOB
            );
        
        CREATE TABLE IF NOT EXISTS course(
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name VARCHAR(32),
            course_week_hours INTEGER
            );
        
        CREATE TABLE IF NOT EXISTS grade(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_no INTEGER,
            course_name VARCHAR(32),
            course_exam_no INTEGER,
            course_grade INTEGER,
            FOREIGN KEY (course_name) REFERENCES course (course_name),
            FOREIGN KEY (student_no) REFERENCES student (student_no)
            );
        """)

def add_course(cursor):
    try:
        entry = input('Enter the course name and weekly course hours (e.g. Physics, 6): ').strip()
        course_name, course_week_hours = entry.split(',')
        cursor.execute("""INSERT INTO course(
            course_name,
            course_week_hours
            )
            VALUES(
                ?,
                ?
                );
        """, (course_name.strip(), int(course_week_hours)))
        
        cursor.connection.commit()        
        print('Course has been successfully added....')
    
    except sqlite3.Error as err:
        print(f"Course hasn't been added. Error: {err}")
    except Exception as err:
        print(f'Invalid entry. Error: {err}')
    print()

def add_student(cursor):
    try:
        entry = input("Enter the student's full name, student number, and the file path of the student's photo (in order and seperated with comma): ").strip()
        student_name, student_no, student_photo = entry.split(',')
        
        with open(os.getcwd() + f'\{student_photo.strip()}', 'rb') as file:
            photo_bytes_obj = file.read()
        
        cursor.execute("""INSERT INTO student(
            student_name,
            student_no,
            student_photo
            )
            VALUES(
                ?,
                ?,
                ?
                );
        """, (student_name.strip(), int(student_no), photo_bytes_obj.strip()))
        
        cursor.connection.commit()        
        print('Student record has been successfully added...')

    except sqlite3.Error as err:
        print(f"Student record hasn't been added. Error: {err}")
    except Exception as err:
        print(f'Invalid entry. Error: {err}')
    print()

def add_grade(cursor):
    try:
        entry = input("Enter the student no, the course name, exam number, and grade in order: ").strip()
        student_no, course_name, course_exam_no, course_grade = entry.split(',')
        
        # Check if there are existing grades for the same student and course
        cursor.execute("""
                       SELECT MAX(course_exam_no)
                       FROM grade
                       WHERE student_no = ? AND course_name = ?;
                       """, (int(student_no), course_name.strip()))
        
        last_exam_no = cursor.fetchone()[0]
        
        if last_exam_no is not None:
            # If there are existing grades, increment the exam number for the new grade
            course_exam_no = int(last_exam_no) + 1
        
        # Insert a new grade entry
        cursor.execute("""INSERT INTO grade(
            student_no,
            course_name,
            course_exam_no,
            course_grade
            )
            VALUES(
                ?,
                ?,
                ?,
                ?
                );
        """, (int(student_no), course_name.strip(), int(course_exam_no), int(course_grade)))
        
        cursor.connection.commit()        
        print('Grade record has been successfully added....')

    except sqlite3.Error as err:
        print(f"Grade record hasn't been added. Error: {err}")
    except Exception as err:
        print(f'Invalid entry. Error: {err}')
    print()

def student_query(cursor):
    try:
        student_no = input("Enter the student's number (press ENTER key for all students): ")
        
        # ENTER key pressed, list all students
        if not student_no:
            cursor.execute("""
                           SELECT student_name, student_no
                           FROM student;
                           """)
        else:
            student_no = int(student_no)
            cursor.execute("""
                           SELECT student_name, student_no
                           FROM student
                           WHERE  student_no = ?;                           
                           """, (student_no, ))
        
        students = cursor.fetchall()
        
        if not students:
            print('No student(s) found.')
            return
        
        for student in students:
            student_name, student_no = student
            print(f'Name: {student_name}')
            print(f'Number: {student_no}\n')
            
            cursor.execute("""
                           SELECT course_name, course_grade
                           FROM grade
                           WHERE student_no = ?;
                           """, (student_no, ))
        
            grades = cursor.fetchall()
            
            if grades:
                cname = {}
                for course_name, grade in grades:
                    cname.setdefault(course_name, []).append(grade)
                
                avg = 0
                total = 0
                for course_name, grade in cname.items():
                    grade2str = ', '.join(map(str, grade))
                    print(f'{course_name}: {grade2str}')
                   
                    cursor.execute("""
                                   SELECT course_week_hours
                                   FROM course
                                   WHERE course_name = ?
                                   """, (course_name, ))
                    
                    course_week_hours = cursor.fetchone()[0]  # convert it to int
                    
                    avg += (sum(grade) / len(grade) * int(course_week_hours))
                    total += int(course_week_hours)

                print(f'\nWeighted Average Grade: {avg / total:.2f}')
            else:
                print('No grades found.')
                
            print('\nPhoto:')
            
            # Fetch the student's photo BLOB from the database
            cursor.execute("""
                           SELECT student_photo
                           FROM student
                           WHERE student_no = ?
                           """, (student_no, ))
            photos = cursor.fetchall()
            
            for photo in photos:
                if photo and photo[0]:
                    # Create an image object from the BLOB using PIL
                    img = Image.open(BytesIO(photo[0]))
                    
                    # Display the image
                    img.show()
                else:
                    print('No photo found.\n')
        
            print('-' * 30)

    except sqlite3.Error as err:
        print(f"Record(s) hasn't been listed **[{err}]**")
    except Exception as err:
        print(f'Invalid entry **[{err}]**')
    print()

def prompt_user_action(cursor):
    while True:
        print('Options:')
        print('1. Course Entry')
        print('2. Student Entry')
        print('3. Grade Entry')
        print('4. Student Query')
        print('5. Exit')
        print()
        
        user_choice = input('Enter the number of your choice: ').strip()
        
        if user_choice == '1':
            add_course(cursor)
        elif user_choice == '2':
            add_student(cursor)
        elif user_choice == '3':
            add_grade(cursor)
        elif user_choice == '4':
            student_query(cursor)
        elif user_choice == '5':
            print('Exiting the database...')
            sys.exit(0)
        else:
            print('Invalid choice. Please enter a valid number (1-5).')

def main():
    try:
        with sqlite3.connect(r'student_notes.sqlite') as connection:
            cursor = connection.cursor()
            generate_tables(cursor)
            prompt_user_action(cursor)
    
    except sqlite3.Error as err:
        print(f'There is an error **[{err}]**')


if __name__ == '__main__':
    main()
    