import os
import sqlite3
import sys


def generate_tables(cursor):
    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS student(
            student_no INTEGER PRIMARY KEY,
            student_name TEXT(64),
            student_photo BLOB
            );
        
        CREATE TABLE IF NOT EXISTS course(
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name VARCHAR(32) UNIQUE,
            course_week_hours INTEGER
            );
        
        CREATE TABLE IF NOT EXISTS grade(
            student_no INTEGER PRIMARY KEY,
            course_name VARCHAR(32),
            course_exam_no INTEGER,
            course_grade INTEGER,
            FOREIGN KEY (course_name) REFERENCES course (course_name),
            FOREIGN KEY (student_no) REFERENCES student (student_no)
            );
        """)

def course_entry(cursor):
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
        print('Record has been successfully added...')
    
    except sqlite3.Error as err:
        print(f"Record hasn't been added **[{err}]**")
    except Exception as err:
        print(f'Invalid entry **[{err}]**')
    print()

def student_entry(cursor):
    try:
        entry = input("Enter the student's full name, student number, and the file path of the student's photo (in order seperated with comma): ").strip()
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
        print('Record has been successfully added...')

    except sqlite3.Error as err:
        print(f"Record hasn't been added **[{err}]**")
    except Exception as err:
        print(f'Invalid entry **[{err}]**')
    print()

def grade_entry(cursor):
    try:
        entry = input("Enter the student no, the course name, exam number, and grade in order: ").strip()
        student_no, course_name, course_exam_no, course_grade = entry.split(',')
                
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
        print('Record has been successfully added...')

    except sqlite3.Error as err:
        print(f"Record hasn't been added **[{err}]**")
    except Exception as err:
        print(f'Invalid entry **[{err}]**')
    print()

def student_query(cursor):
    try:
        student_no = int(input("Enter the student's number: "))
                
        if not student_no:
            pass

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
            course_entry(cursor)
        elif user_choice == '2':
            student_entry(cursor)
        elif user_choice == '3':
            grade_entry(cursor)
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