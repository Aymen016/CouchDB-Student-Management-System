import requests
from requests.auth import HTTPBasicAuth

# CouchDB URL
COUCHDB_URL = "http://localhost:5984"  # your CouchDB instance
DB_NAME = "students"  # The name of the database
USERNAME = "admin"  # your CouchDB admin username
PASSWORD = "admin" 

# Create database
# Create a CouchDB database
def create_database():
    response = requests.put(f"{COUCHDB_URL}/{DB_NAME}", auth=(USERNAME, PASSWORD))
    if response.status_code == 201:
        print(f"Database '{DB_NAME}' created successfully.")
    elif response.status_code == 412:
        print(f"Database '{DB_NAME}' already exists.")
    else:
        print(f"Failed to create database: {response.status_code}, {response.text}")

#create_database()

def add_student(student_data):
    # Add a document to the database
    response = requests.post(f"{COUCHDB_URL}/{DB_NAME}", json=student_data, auth=(USERNAME, PASSWORD))
    if response.status_code == 201:
        print(f"Student added successfully: {response.json()}")
    else:
        print(f"Failed to add student: {response.status_code}, {response.text}")

# Sample student data
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science"
}

#add_student(student)

def get_student_by_id(doc_id):
    # Get a document by its _id
    response = requests.get(f"{COUCHDB_URL}/{DB_NAME}/{doc_id}", auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        print(f"Student retrieved: {response.json()}")
    else:
        print(f"Failed to retrieve student: {response.status_code}, {response.text}")

# Example: Replace with the actual _id of the document you want to retrieve
#
# doc_id = "600d964f940d27277dad256079003664"  # Replace with the actual document ID
#get_student_by_id(doc_id)

# Update a student's age
def update_student_age(doc_id, new_age):
    # Step 1: Retrieve the existing document
    response = requests.get(f"{COUCHDB_URL}/{DB_NAME}/{doc_id}", auth=(USERNAME, PASSWORD))
    if response.status_code == 200:
        document = response.json()  # Get the existing document
        
        # Step 2: Update the age while preserving other fields
        document["age"] = new_age  # Update the age
        
        # Step 3: Send the updated document back to CouchDB
        update_response = requests.put(
            f"{COUCHDB_URL}/{DB_NAME}/{doc_id}",
            json=document,
            auth=(USERNAME, PASSWORD)
        )
        if update_response.status_code == 201:
            print(f"Student updated successfully: {update_response.json()}")
        else:
            print(f"Failed to update student: {update_response.status_code}, {update_response.text}")
    else:
        print(f"Failed to retrieve student: {response.status_code}, {response.text}")




# Delete a student
def delete_student(doc_id, rev):
    # Deleting requires both _id and _rev
    response = requests.delete(
        f"{COUCHDB_URL}/{DB_NAME}/{doc_id}?rev={rev}",
        auth=(USERNAME, PASSWORD)
    )
    if response.status_code == 200:
        print(f"Student deleted successfully: {response.json()}")
    else:
        print(f"Failed to delete student: {response.status_code}, {response.text}")

# Example usage
doc_id = "600d964f940d27277dad256079003664" 
doc_rev = "2-4e0db242a69135cb570c10503cfa03a4"  

# Update student age
update_student_age(doc_id, 25, doc_rev)

# Delete student
delete_student(doc_id, doc_rev)