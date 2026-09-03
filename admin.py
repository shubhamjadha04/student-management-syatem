from database import cursor,conn
import mysql.connector
from auth import(
    validate_email,
    email_exists,
)

# adding all details of the student in students table
def add_student_detail(user_id):
    roll_no = input("Enter Roll no.: ")
    phone = input("Enter phone no.: ")
    address = input("Enter address: ")
    gender = input("Enter gender: ")
    dob = input("Enter date of birth: ")
    branch = input("Enter Branch: ")
    add_year =  input("Enter addimission year: ")


    query = """
              INSERT INTO students(user_id,roll_no,phone,address, gender, dob, branch, admission_year)
              VALUES(%s,%s,%s,%s,%s,%s,%s,%s)  
                """

    cursor.execute(query,(user_id,roll_no,phone,address,gender,dob,branch,add_year))
    conn.commit()
    print("The details addes successfully.")


# this is the admin menu 

def add_student():
    try:
        name =input("Enter your Name: ")
        email = input("Enter your Email: ")
        
        # valid emia; check
        if not validate_email(email):
            raise ValueError ("Enter valid Email.")
                
        # email already present check
        if email_exists(email):
            raise ValueError ("Email Already exists..")
        
        print("Password must have at least 8 characters.")
        pwd = input("Enter your password: ")
        
        # validate the password
        if len(pwd) < 8:
             raise ValueError("The Password should have 8 letters... ")

        query = """
                    INSERT INTO users(name,email,password,role)
                    VALUES(%s,%s,%s,%s)
                """
        cursor.execute(query,(name,email,pwd,'student'))
        conn.commit()

        user_id = cursor.lastrowid
        print("Student added Successfully..\n add other details.")
        add_student_detail(user_id)
        
        
# exception handling
    except ValueError as e:
        print("Error",e)
        return None

    except mysql.connector.Error as e:
        print("Error",e)
        return None
  
# view all student from the users table

def view_all_students():
    query = """
        SELECT user_id, name, email
        FROM users
        WHERE role = 'student'
    """

    cursor.execute(query)
    students = cursor.fetchall()

    print("\n========== ALL STUDENTS ==========")
    print(f"{'ID':<10}{'NAME':<20}{'EMAIL':<30}")
    print("-" * 60)

    for student in students:
        print(f"{student[0]:<10}{student[1]:<20}{student[2]:<30}")

    print("=" * 60)


# update_student function 

def update_student():
    try:
        view_all_students()

        user_id = input("Enter the id of the student want to update: ")
        # checking the student is present
        check_query = """
            SELECT user_id
            FROM students
            WHERE user_id = %s
        """

        cursor.execute(check_query, (user_id,))
        student = cursor.fetchone()

        if student is None:
            print("Student ID not found.")
            return


        roll_no = input("Enter Roll no.: ")
        phone = input("Enter phone no.: ")
        address = input("Enter address: ")
        gender = input("Enter gender: ")
        dob = input("Enter date of birth: ")
        branch = input("Enter Branch: ")
        add_year =  input("Enter addimission year: ")
        
        
        query = """
                    UPDATE students 
                    SET roll_no = %s,
                        phone = %s,
                        address = %s,
                        gender= %s,
                        dob =%s,
                        branch = %s,
                        admission_year = %s

                    WHERE user_id = %s 
                        """
        
        cursor.execute(query,(roll_no,phone,address,gender,dob,branch,add_year,user_id))
        conn.commit()
        print("The Student details updated successfully.")

    except mysql.connector.Error as e:
        print("Error",e)
        


def delete_student():
    try:      
        view_all_students()

        user_id = input("Enter Id of the student which you want to delete: ")
        query1 = """
                    DELETE FROM students 
                    WHERE user_id = %s"""

        query2 = """
                        DELETE FROM  users
                        WHERE user_id = %s"""

    

        cursor.execute(query1,(user_id,))

        
        if cursor.rowcount == 0:
            print("Student not found.")
            conn.rollback()
            return

        cursor.execute(query2,(user_id,))
        conn.commit()

        print("The student deleted successfully..")

    except mysql.connector.Error as e:
        print("Error",e)
    
# add add_course function
def add_course():
    try:
        course_name = input("Enter the course name: ")
        course_code = input("Enter the course code: ")

        # checking ciurse code 
        check_code = """SELECT course_name 
                        FROM courses WHERE
                        course_code = %s"""
        cursor.execute(check_code,(course_code,))
        check = cursor.fetchone()

        if check:
            print("course code alrady exists.")
            return

        credits = int(input("Enter the credits: "))

        if credits < 0:
            raise ValueError("Credits must be greater than 0.")

        query = """
                   INSERT INTO courses(course_name,course_code,credits)
                   VALUES(%s,%s,%s)                     
                """

        cursor.execute(query,(course_name,course_code,credits))
        conn.commit()

        print("The course added succeffully..")


    except ValueError:
        print("The credits must be numbers.")

    except mysql.connector.Error as e:
        conn.rollback()
        print("Error",e)



def add_teacher():
    pass

def manage_attendance():
    pass


def reports():
    pass