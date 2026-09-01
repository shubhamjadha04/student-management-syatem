from database import cursor,conn
import mysql.connector



# user register function
def user_register():
    try:      
        name =input("Enter your Name: ")
        email = input("Enter your Email: ")
        print("Password should have 8 letters...")
        pwd = input("Enter your password: ")
        role = input("Enter your Role: ").lower()

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

        print("You have successfully Register.")


# excception handling
    except ValueError as e:
        print("Error",e)   

    except mysql.connector.Error as e:
        print("Database error:", e)



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

        else:
            print("Email or Password is wrong..")

    except mysql.connector.Error as e:
        print("Database error:", e)


# the register and the login menu:

while True:
    print("----Welcome to the Student Management System----")
    print("\n1. Register.")
    print("2. Login.")
    print("3. To Exit.")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_register()

    elif choice == "2":
        user_login()

    elif choice == "3":
        print("Thank you..\nExit")
        break

    else:
        print("Invalid Option. ")


        
