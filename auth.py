from database import cursor,conn
import mysql.connector

# user register function
def user_register():
    try:      
        name =input("Enter your Name: ")
        email = input("Enter your Email: ")
        print("Password should have 8 letters...")
        pwd = input("Enter your password: ")
        role = input("Enter the role: ").lower()
        

        if len(pwd) < 8:
            raise ValueError("The Password should have 8 letters... ")
        
        if not email.endswith("@gmail.com"):
            raise ValueError ("Enter valid Email.")

        if role not in ('student', "admin"):
            raise ValueError ("Enter Valid Role..")

        query = """
                INSERT INTO users (name,email,password,role)
                VALUES(%s,%s,%s,%s)
                 """

    
        cursor.execute(query,(name,email,pwd,role))
        conn.commit()

        user_id = cursor.lastrowid

        print("You have successfully Register.")
        return user_id, role
        


# excception handling
    except ValueError as e:
        print("Error",e)   
        return None

    except mysql.connector.Error as e:
        print("Database error:", e)
        return None



# user login function 
def user_login():
    try:    
        email = input("Enter Your email: ")
        pwd = input("Enter Your password:  ")

        query = """
                SELECT user_id,role FROM
                users WHERE  email = %s and password = %s"""

        cursor.execute(query,(email,pwd))

        user = cursor.fetchone()

        if user:
            user_id = user[0]
            role = user[1]
            print("Login Successfull..")
            return user_id,role

        else:
            print("Email or Password is wrong..")
            return None

    except mysql.connector.Error as e:
        print("Database error:", e)
        return None