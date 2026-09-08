from database import cursor,conn
import mysql.connector
from auth import(
    validate_email,
    email_exists,
)


# view_courses FUNCTION
def view_courses(user_id):
    pass
   


# view_profile FUNCTION
def view_profile(user_id):
    query = """
                SELECT
                s.student_id, 
                u.name,
                u.email,
                s.roll_no,
                s.phone,
                s.address,
                s.gender,
                s.dob,
                s.branch,
                s.admission_year
                FROM users u
                join students s
                on u.user_id = s.user_id
                WHERE u.user_id = %s
            """
    
    cursor.execute(query,(user_id,))
    student = cursor.fetchone()
    
    if not student:
        print("Student Not Found!!")
        return
    
    print("\n========== MY PROFILE ==========")
    print(f"Student ID      : {student[0]}")
    print(f"Name            : {student[1]}")
    print(f"Email           : {student[2]}")
    print(f"Roll No         : {student[3]}")
    print(f"Phone           : {student[4]}")
    print(f"Address         : {student[5]}")
    print(f"Gender          : {student[6]}")
    print(f"Date of Birth   : {student[7]}")
    print(f"Branch          : {student[8]}")
    print(f"Admission Year  : {student[9]}")
    print("=" * 35)


# view_marks FUNCTION
def view_marks():
    pass


# # view_attendance FUNCTION
# def view_attendance():
#     pass



