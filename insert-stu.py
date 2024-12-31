import requests
import random
import string

# CouchDB details
COUCHDB_URL = "http://localhost:5984"  # Replace with your CouchDB URL
DB_NAME = "students"
USERNAME = "admin"  
PASSWORD = "admin"  

# Function to generate random student data
def generate_student_data():
    first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    majors = ["Mathematics", "Computer Science", "Physics", "Biology", "Engineering", "Art", "History", "Psychology"]
    
    # Generate random student data
    students = []
    for _ in range(100):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        age = random.randint(18, 25)
        major = random.choice(majors)
        student = {
            "_id": ''.join(random.choices(string.ascii_lowercase + string.digits, k=24)),  # Random unique ID
            "name": name,
            "age": age,
            "major": major
        }
        students.append(student)
    return students

# Insert multiple students into CouchDB
def insert_students_bulk(students):
    # Bulk insert into CouchDB
    response = requests.post(
        f"{COUCHDB_URL}/{DB_NAME}/_bulk_docs",
        json={"docs": students},
        auth=(USERNAME, PASSWORD)
    )
    if response.status_code == 201:
        print("Students added successfully.")
    else:
        print(f"Failed to insert students: {response.status_code}, {response.text}")

# Generate and insert 100 students
students = generate_student_data()
insert_students_bulk(students)
