from database import cursor,conn
import mysql.connector
from auth import(
    validate_email,
    email_exists,
)
# view profile
def teacher_profile(user_id):
    try:
        query = """
            SELECT 
                t.teacher_id,
                u.name,
                u.email,
                t.phone,
                t.branch
            FROM users u
            JOIN teachers t
                ON u.user_id = t.user_id
            WHERE u.user_id = %s
        """

        cursor.execute(query, (user_id,))
        teacher = cursor.fetchone()

        if teacher is None:
            print("Teacher profile not found.")
            return

        print("\n========== MY PROFILE ==========")
        print(f"Teacher ID : {teacher[0]}")
        print(f"Name       : {teacher[1]}")
        print(f"Email      : {teacher[2]}")
        print(f"Phone      : {teacher[3]}")
        print(f"Branch     : {teacher[4]}")
        print("================================")

    except mysql.connector.Error as e:
        print("Error:", e)


# view my ourses
def view_my_courses(teacher_id):
    try:
        query = """
            SELECT 
                c.course_id,
                c.course_name,
                c.course_code,
                c.credits
            FROM users u
            JOIN teachers t
                ON u.user_id = t.user_id
            JOIN teacher_course tc
                ON t.teacher_id = tc.teacher_id
            JOIN courses c
                ON c.course_id = tc.course_id
            WHERE u.user_id = %s
        """

        cursor.execute(query, (user_id,))
        courses = cursor.fetchall()

        if not courses:
            print("No courses assigned to you.")
            return

        print("\n========== MY COURSES ==========")
        print(f"{'ID':<10}{'COURSE NAME':<25}{'CODE':<15}{'CREDITS':<10}")
        print("-" * 60)

        for course in courses:
            print(
                f"{course[0]:<10}"
                f"{course[1]:<25}"
                f"{course[2]:<15}"
                f"{course[3]:<10}"
            )

        print("=" * 60)

    except mysql.connector.Error as e:
        print("Error:", e)





#  view enrolled students
def view_enrolled_students(teacher_id):
    pass


# marks menu
def marks_menu(teacher_id):
    pass


# attendence menu
def attendance_menu(teacher_id):
    pass



