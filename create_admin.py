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





# user register function
def user_register():
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
                INSERT INTO users (name,email,password,role)
                VALUES(%s,%s,%s,%s)
                 """

    
        cursor.execute(query,(name,email,pwd,"admin"))
        conn.commit()

        user_id = cursor.lastrowid

        print("You have successfully Register.")
        return user_id
        


# excception handling
    except ValueError as e:
        print("Error",e)   
        return None

    except mysql.connector.Error as e:
        print("Database error:", e)
        return None

user_register()