from flask import Flask, request, render_template, redirect, url_for, jsonify
from services import student_service
from data import repository

app = Flask(__name__)
repository.create_tables()

@app.route("/")
def index():
    students = student_service.get_students()
    courses = student_service.get_courses()
    enrollments = student_service.get_enrollments()
    return render_template("index.html", students=students, courses=courses, enrollments=enrollments)

# --- Browser Form Routes ---

@app.route("/add_student_form", methods=["POST"])
def add_student_form():
    name = request.form.get("name")
    if name: student_service.add_student(name)
    return redirect(url_for("index"))

@app.route("/add_course_form", methods=["POST"])
def add_course_form():
    name = request.form.get("name")
    if name: student_service.add_course(name)
    return redirect(url_for("index"))

@app.route("/enroll_form", methods=["POST"])
def enroll_form():
    s_id = request.form.get("student_id")
    c_id = request.form.get("course_id")
    if s_id and c_id:
        student_service.enroll_student(int(s_id), int(c_id))
    return redirect(url_for("index"))

@app.route("/delete_enroll_form/<int:student_id>")
def delete_enroll_form(student_id):
    student_service.delete_student(student_id)
    return redirect(url_for("index"))

@app.route("/delete_student_form/<int:student_id>")
def delete_student_form(student_id):
    student_service.delete_student(student_id)
    return redirect(url_for("index"))

@app.route("/delete_course_form/<int:course_id>")
def delete_course_form(course_id):
    student_service.delete_course(course_id)
    return redirect(url_for("index"))

# --- JSON API Routes (Optional) ---

@app.route("/students", methods=["GET"])
def get_students_api():
    return jsonify(student_service.get_students())

@app.route("/enrollments", methods=["GET"])
def get_enrollments_api():
    return jsonify(student_service.get_enrollments())

if __name__ == "__main__":
    app.run(debug=True)