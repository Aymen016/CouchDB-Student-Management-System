# 🎓 Student Management System with Flask & CouchDB

This project is a web-based Student Management System built using **Flask** and **CouchDB**. It allows users to create, read, update, and delete student records, with features like bulk data insertion and detailed student views.

<img width="1024" height="1024" alt="ChatGPT Image Jul 24, 2025, 11_57_06 AM" src="https://github.com/user-attachments/assets/401a7270-9df7-4c5a-95b2-8d01746486da" />

---

## 🧠 What is CouchDB?

**Apache CouchDB** is a **NoSQL document-oriented database** that stores data in **JSON format**. Unlike traditional SQL databases, CouchDB:

- Uses a RESTful HTTP API for data access and manipulation
- Stores documents with dynamic fields (no predefined schema)
- Automatically manages document versions using `_rev` field
- Is ideal for apps needing offline support, replication, or a flexible data model

> In this project, CouchDB is used to store and manage student records. Each student is a separate JSON document with fields like `name`, `age`, and `major`.

---

## 🚀 Features

- 🧑‍🎓 View all students
- ➕ Add new students via form
- 📦 Bulk insert 100 random student records
- 🔍 View details of a single student
- 📝 Update student age
- 🗑️ Delete a student record
- 📱 Responsive UI (via HTML templates)

---

## 🛠️ Tech Stack

| Category      | Tools / Libraries               |
|---------------|---------------------------------|
| Backend       | Python, Flask                   |
| Database      | CouchDB (NoSQL)                 |
| HTTP Client   | `requests` module (for DB calls)|
| Frontend      | HTML + Jinja2 templates         |

---

## 🗂️ Folder Structure

```bash
project/
│
├── templates/
│ ├── index-co.html
│ ├── students.html
│ └── student_detail.html
├── app.py
├── requirements.txt
```


---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-flask-couchdb.git
cd student-flask-couchdb
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Configure CouchDB

Make sure you have CouchDB running locally at [http://localhost:5984](http://localhost:5984) with the following details:

- **Database Name:** `students`  
- **Username:** `admin`  
- **Password:** `admin`  

Update these in your `app.py` file if necessary:

```python
COUCHDB_URL = "http://localhost:5984"
DB_NAME = "students"
USERNAME = "admin"
PASSWORD = "admin"
```

### 5. Run the App

Start the Flask application by running:

```bash
python app.py
```

Then open your browser and visit: [http://localhost:8080](http://localhost:8080)

---

## 🌐 Available Routes

| Route                | Method | Description                        |
|----------------------|--------|------------------------------------|
| `/`                  | GET    | Home page                          |
| `/students`          | GET    | View all student records           |
| `/add_student`       | POST   | Add a new student                  |
| `/insert_students`   | POST   | Insert 100 random students         |
| `/get_student`       | GET    | View individual student details    |
| `/update_student_age`| POST   | Update a student's age             |
| `/delete_student`    | POST   | Delete a student by ID             |

---

## 📌 Notes

- CouchDB must be running and accessible during development.
- The `_id` field for each student is a random 24-character string.
- Sample fields include `name`, `age`, and `major`.

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 🤝 Author

**Aymen Baig**  
📧 [ayemenbaig26@gmail.com](mailto:ayemenbaig26@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/aymen-baig-700a06284/) <br>
🔗 [GitHub](https://github.com/Aymen016)

---

## 🌟 Support

If you find this project helpful, feel free to ⭐ star the repo or contribute by submitting a pull request!




