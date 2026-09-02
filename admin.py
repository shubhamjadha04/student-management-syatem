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
        
        



    except ValueError as e:
        print("Error",e)
        return None

    except mysql.connector.Error as e:
        print("Error",e)
        return None

    

    


def update_student():
    pass


def delete_student():
    pass

def add_course():
    pass


def manage_marks():
    pass

def manage_attendance():
    pass


def reports():
    pass