from database import cursor,conn
import mysql.connector

# user register function
def user_register():
    try:      
        name =input("Enter your Name: ")
        email = input("Enter your Email: ")
        print("Password should have 8 letters...")
        pwd = input("Enter your password: ")
        

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

        


        cursor.execute(query,(name,email,pwd,"student"))
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



# user login function 
def user_login():
    try:    
        email = input("Enter Your email: ")
        pwd = input("Enter Your password:  ")

        query = """
                SELECT user_id FROM
                users WHERE  email = %s and password = %s"""

        cursor.execute(query,(email,pwd))

        user_id = cursor.fetchone()

        if user_id:
            print("Login Successfull..")
            print("User Id: ",user_id[0])
            return user_id[0]

        else:
            print("Email or Password is wrong..")
            return None

    except mysql.connector.Error as e:
        print("Database error:", e)
        return None