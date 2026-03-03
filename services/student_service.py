from data import repository
import sqlite3

def add_student(name):
    repository.execute_query("INSERT INTO students (name) VALUES (?)", (name,))

def get_students():
    return repository.fetch_query("SELECT * FROM students")

def delete_student(student_id):
    repository.execute_query("DELETE FROM students WHERE id = ?", (student_id,))

def add_course(name):
    repository.execute_query("INSERT INTO courses (name) VALUES (?)", (name,))

def get_courses():
    return repository.fetch_query("SELECT * FROM courses")

def delete_course(course_id):
    repository.execute_query("DELETE FROM courses WHERE id = ?", (course_id,))

def enroll_student(student_id, course_id):
    try:
        repository.execute_query("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
        return True
    except sqlite3.IntegrityError:
        return False

def get_enrollments():
    return repository.fetch_query("""
        SELECT students.name AS student_name, courses.name AS course_name
        FROM enrollments
        JOIN students ON enrollments.student_id = students.id
        JOIN courses ON enrollments.course_id = courses.id
    """)