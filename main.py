from database import cursor,conn
import mysql.connector


def user_register():
    try:      
        name =input("Enter your Name: ")
        email = input("Enter your Email: ")
        print("Password should have 8 letters...")
        pwd = input("Enter your password: ")
        role = input("Enter your Role: ")

        if len(pwd) > 8:
            raise ValueError("The Password should have 8 letters... ")
        
        if not email.endswith("@gmail.com"):
            raise ValueError ("Enter valid Email.")

        if role not in ('student', "admin"):
            raise ValueError ("Enter Valid Role..")

        print("You have successfully Register.")

        query = """
                INSERT INTO users (name,email,password,role)
                VALUES(%s,%s,%s,%s)
                 """

        cursor.execute(query,(name,email,pwd,role))
        conn.commit()


    except ValueError as e:
        print("Error",e)

    

    except mysql.connector.Error as e:
        print("Database error:", e)

user_register()