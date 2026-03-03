import sqlite3

DB_NAME = "database.db"


def get_connection():
    # timeout=10 helps prevent "database is locked" errors
    conn = sqlite3.connect(DB_NAME, timeout=10)
    # Enable foreign keys to support ON DELETE CASCADE
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")

    cursor.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL)")

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS enrollments
                   (
                       student_id
                       INTEGER,
                       course_id
                       INTEGER,
                       PRIMARY
                       KEY
                   (
                       student_id,
                       course_id
                   ),
                       FOREIGN KEY
                   (
                       student_id
                   ) REFERENCES students
                   (
                       id
                   ) ON DELETE CASCADE,
                       FOREIGN KEY
                   (
                       course_id
                   ) REFERENCES courses
                   (
                       id
                   )
                     ON DELETE CASCADE
                       )
                   """)
    conn.commit()
    conn.close()


def execute_query(query, params=()):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    finally:
        conn.close()


def fetch_query(query, params=()):
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()