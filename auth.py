from database import cursor,conn
import mysql.connector
import re


# validate_email fuction
def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@gmail\.com$'
    return re.match(pattern, email)


# email present function
def email_exists(email):
    query = "SELECT 1 FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    return cursor.fetchone() is not None


# user login function 
def admin_login():
    try:    
        email = input("Enter Your email: ")
        pwd = input("Enter Your password:  ")

        query = """
                SELECT user_id FROM
                users WHERE  email = %s and password = %s and role = 'admin'
                """

        cursor.execute(query,(email,pwd))

        user= cursor.fetchone()

        if user:
            user_id = user[0]
            
            print("Login Successfull..")
            print("Your user id is ",user_id)
            return user_id

        else:
            print("Email or Password is wrong..")
            return None

    except mysql.connector.Error as e:
        print("Database error:", e)
        return None




def student_login():
    try:    
        email = input("Enter Your email: ")
        pwd = input("Enter Your password:  ")

        query = """
                SELECT user_id FROM
                users WHERE  email = %s and password = %s  and role = 'student'
                 """

        cursor.execute(query,(email,pwd))

        user = cursor.fetchone()
        if user:
            user_id = user[0]
            print("Login Successfull..")
            print("Your user id is ",user_id)
            return user_id


        else:
            print("Email or Password is wrong..")
            return None

    except mysql.connector.Error as e:
        print("Database error:", e)
        return None