from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)


# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students")
def get_students():
    """
    Route to fetch all students from the database
    return: Array of student objects
    """
    return jsonify(db.get_all_students()), 200


@app.route("/students", methods=["POST"])
def create_student():
    """
    Route to create a new student
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The created student if successful
    """

    # Getting the request body - replace with your implementation
    student_data = request.json

    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")

    if not name:
        return jsonify({"error": "name is required"}), 404
    if not course:
        return jsonify({"error": "course is required"}), 404

    new_student = db.insert_student(name, course, mark)

    return jsonify(new_student), 200


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """
    Route to update student details by id
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The updated student if successful
    """

    student_data = request.json

    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")

    updated_student = db.update_student(student_id, name, course, mark)
    if updated_student is None:
        return jsonify({"error": "invalid student id"}), 404

    return jsonify(updated_student), 200


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """
    Route to delete student by id
    return: The deleted student
    """
    deleted_student = db.delete_student(student_id)

    if deleted_student is None:
        return jsonify({"error": "invalid student id"}), 404

    return jsonify(deleted_student), 200


@app.route("/stats")
def get_stats():
    """
    Route to show the stats of all student marks 
    return: An object with the stats (count, average, min, max)
    """
    student_data = db.get_all_students()

    marks = []
    for student in student_data:
        if student["mark"] is not None:
            marks.append(student["mark"])

    if len(marks) == 0:
        return jsonify({"count": 0, "average": None, "min": None, "max": None}), 200

    return jsonify({
        "count": len(marks),
        "average": sum(marks) / len(marks),
        "min": min(marks),
        "max": max(marks)
    }), 200


@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
