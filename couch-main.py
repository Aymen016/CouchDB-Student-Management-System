from flask import Flask, request, jsonify, render_template, redirect
import requests
import random
import string

app = Flask(__name__)

# CouchDB details
COUCHDB_URL = "http://localhost:5984"
DB_NAME = "students"
USERNAME = "admin"  # Replace with your CouchDB admin username
PASSWORD = "admin"  # Replace with your CouchDB admin password


@app.route('/students', methods=['GET'])
def get_students():
    response = requests.get(f"{COUCHDB_URL}/{DB_NAME}/_all_docs?include_docs=true", auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        data = response.json()
        students = [row["doc"] for row in data["rows"]]
        return render_template('students.html', students=students)
    else:
        return f"Failed to fetch students: {response.status_code}, {response.text}"

# Bulk insert students
@app.route('/insert_students', methods=['POST'])
def insert_students():
    students = generate_student_data()
    response = requests.post(
        f"{COUCHDB_URL}/{DB_NAME}/_bulk_docs",
        json={"docs": students},
        auth=(USERNAME, PASSWORD)
    )
    if response.status_code == 201:
        return jsonify({"message": "Students added successfully."}), 201
    else:
        return jsonify({"error": response.text}), response.status_code

# Generate random student data
def generate_student_data():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown"]
    majors = ["Mathematics", "Computer Science", "Physics", "Biology", "Engineering"]
    students = []
    for _ in range(100):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 25)
        major = random.choice(majors)
        student = {
            "_id": ''.join(random.choices(string.ascii_lowercase + string.digits, k=24)),
            "name": name,
            "age": age,
            "major": major
        }
        students.append(student)
    return students


@app.route('/')
def index():
    return render_template('index-co.html')
# Fetch all students
@app.route('/add_student', methods=['POST'])
def add_student():
    # Retrieve data from the form
    name = request.form.get('name')
    age = request.form.get('age')
    major = request.form.get('major')

    # Prepare the student data
    student_data = {
        "name": name,
        "age": int(age),
        "major": major
    }

    # Insert into CouchDB
    response = requests.post(
        f"{COUCHDB_URL}/{DB_NAME}",
        json=student_data,
        auth=(USERNAME, PASSWORD)
    )

    # Check if the insertion was successful
    if response.status_code == 201:
        success_message = "Student added successfully."

        # Fetch all students from CouchDB
        student_response = requests.get(
            f"{COUCHDB_URL}/{DB_NAME}/_all_docs?include_docs=true",
            auth=(USERNAME, PASSWORD)
        )

        if student_response.status_code == 200:
            students = [
                row["doc"] for row in student_response.json().get("rows", [])
            ]
            return render_template('students.html', success_message=success_message, students=students)
        else:
            error_message = "Failed to fetch student list."
            return render_template('students.html', error_message=error_message)
    else:
        error_message = f"Failed to add student: {response.status_code}, {response.text}"
        return render_template('students.html', error_message=error_message)
    

@app.route('/get_student', methods=['GET'])
def get_student():
    student_id = request.args.get('student_id')

    # Retrieve the student from CouchDB
    response = requests.get(
        f"{COUCHDB_URL}/{DB_NAME}/{student_id}",
        auth=(USERNAME, PASSWORD)
    )

    if response.status_code == 200:
        student = response.json()
        return render_template('student_detail.html', student=student)
    else:
        error_message = f"Failed to retrieve student: {response.status_code}, {response.text}"
        return render_template('student_detail.html', error_message=error_message)
    
@app.route('/update_student_age', methods=['POST'])
def update_student_age():
    student_id = request.form.get('student_id')
    new_age = request.form.get('new_age')

    # Retrieve the current student document
    response = requests.get(
        f"{COUCHDB_URL}/{DB_NAME}/{student_id}",
        auth=(USERNAME, PASSWORD)
    )

    if response.status_code == 200:
        student = response.json()
        student['age'] = int(new_age)  # Update the age

        # Send the updated document back to CouchDB
        update_response = requests.put(
            f"{COUCHDB_URL}/{DB_NAME}/{student_id}",
            json=student,
            auth=(USERNAME, PASSWORD)
        )

        if update_response.status_code == 201:
            success_message = "Student age updated successfully."
            return render_template('student_detail.html', student=student, success_message=success_message)
        else:
            error_message = f"Failed to update student: {update_response.status_code}, {update_response.text}"
            return render_template('student_detail.html', error_message=error_message)
    else:
        error_message = f"Failed to retrieve student: {response.status_code}, {response.text}"
        return render_template('student_detail.html', error_message=error_message)
@app.route('/delete_student', methods=['POST'])
def delete_student():
    student_id = request.form.get('student_id')

    # Retrieve the current student document
    response = requests.get(
        f"{COUCHDB_URL}/{DB_NAME}/{student_id}",
        auth=(USERNAME, PASSWORD)
    )

    if response.status_code == 200:
        student = response.json()
        rev = student['_rev']

        # Delete the student document
        delete_response = requests.delete(
            f"{COUCHDB_URL}/{DB_NAME}/{student_id}?rev={rev}",
            auth=(USERNAME, PASSWORD)
        )

        if delete_response.status_code == 200:
            success_message = "Student deleted successfully."
            return redirect('/students')
        else:
            error_message = f"Failed to delete student: {delete_response.status_code}, {delete_response.text}"
            return render_template('student_detail.html', error_message=error_message)
    else:
        error_message = f"Failed to retrieve student: {response.status_code}, {response.text}"
        return render_template('student_detail.html', error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
