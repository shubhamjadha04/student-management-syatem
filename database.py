import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'shubham2004',
    database = 'student_management'
)

cursor = conn.cursor()
