# Student Management System

A command-line Student Management System built using Python and MySQL. The application provides role-based access for administrators, teachers, and students to manage academic information, courses, enrollments, marks, and attendance.

## Features

### Admin

* Register and manage students
* Add, update, view, and delete teachers
* Add and manage courses
* Assign teachers to courses
* Enroll students in courses

### Teacher

* View profile
* View assigned courses
* View enrolled students
* Add, update, view, and delete marks
* Manage attendance

### Student

* View personal profile
* View enrolled courses
* View marks
* View attendance

## Technologies Used

* Python
* MySQL
* mysql-connector-python
* SQL
* Command Line Interface

## Database Concepts Used

* Primary keys and foreign keys
* One-to-one and one-to-many relationships
* Many-to-many relationships
* JOIN operations
* Parameterized SQL queries
* Constraints such as `UNIQUE`, `NOT NULL`, and `AUTO_INCREMENT`

## Project Structure

```text
student-management-syatem/
│
├── main.py
├── database.py
├── auth.py
├── admin.py
├── teacher.py
├── student.py
├── marks.py
├── attendance.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository.
2. Create the MySQL database.
3. Create the required tables.
4. Update the database credentials in `database.py`.
5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application:

```bash
python main.py
```

## Future Improvements

* Password hashing
* Better input validation
* Attendance percentage calculation
* Export reports to CSV or PDF
* Graphical or web-based interface
* Improved database configuration using environment variables

