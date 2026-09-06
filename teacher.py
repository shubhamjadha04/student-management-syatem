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
def view_my_courses(user_id):
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
    try:
        query = """
            SELECT
                s.student_id,
                su.name,
                su.email,
                c.course_name
            FROM users u

            JOIN teachers t
                ON u.user_id = t.user_id

            JOIN teacher_course tc
                ON t.teacher_id = tc.teacher_id

            JOIN courses c
                ON tc.course_id = c.course_id

            JOIN enrollments e
                ON c.course_id = e.course_id

            JOIN students s
                ON e.student_id = s.student_id

            JOIN users su
                ON s.user_id = su.user_id

            WHERE u.user_id = %s
            ORDER BY c.course_name, su.name
        """

        cursor.execute(query, (teacher_id,))
        students = cursor.fetchall()

        if not students:
            print("\nNo students are enrolled in your courses.")
            return

        print("\n==================== MY STUDENTS ====================")
        print(f"{'ID':<10}{'NAME':<20}{'EMAIL':<30}{'COURSE':<20}")
        print("-" * 80)

        for student in students:
            print(
                f"{student[0]:<10}"
                f"{student[1]:<20}"
                f"{student[2]:<30}"
                f"{student[3]:<20}"
            )

        print("=" * 80)

    except mysql.connector.Error as e:
        print("Error:", e)


# marks menu
def marks_menu(teacher_id):
    pass


# attendence menu
def attendance_menu(teacher_id):
    pass



