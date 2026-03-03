from services import student_service


def seed():
    print("🌱 Seeding database...")

    # Add some students
    students = ["Alice Smith", "Bob Jones", "Charlie Brown", "Diana Prince"]
    for name in students:
        student_service.add_student(name)
        print(f"Added student: {name}")

    # Add some courses
    courses = ["Python 101", "Web Development", "Database Design"]
    for course in courses:
        student_service.add_course(course)
        print(f"Added course: {course}")

    # Enrollments (Student ID 1 in Course 1, etc.)
    # Note: IDs start at 1 in a fresh database
    student_service.enroll_student(1, 1)
    student_service.enroll_student(1, 2)
    student_service.enroll_student(2, 1)

    print("✅ Seeding complete! Refresh your browser.")


if __name__ == "__main__":
    seed()