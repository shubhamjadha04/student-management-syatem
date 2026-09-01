from database import cursor,conn
import mysql.connector
from auth import user_login,user_register



# # user register function
# def user_register():
#     try:      
#         name =input("Enter your Name: ")
#         email = input("Enter your Email: ")
#         print("Password should have 8 letters...")
#         pwd = input("Enter your password: ")
#         role = input("Enter your Role: ").lower()

#         if len(pwd) < 8:
#             raise ValueError("The Password should have 8 letters... ")
        
#         if not email.endswith("@gmail.com"):
#             raise ValueError ("Enter valid Email.")

#         if role not in ('student', "admin"):
#             raise ValueError ("Enter Valid Role..")

#         query = """
#                 INSERT INTO users (name,email,password,role)
#                 VALUES(%s,%s,%s,%s)
#                  """

#         cursor.execute(query,(name,email,pwd,role))
#         conn.commit()

#         print("You have successfully Register.")
#         search_student()


# # excception handling
#     except ValueError as e:
#         print("Error",e)   

#     except mysql.connector.Error as e:
#         print("Database error:", e)



# # user login function 
# def user_login():
#     try:    
#         email = input("Enter Your email: ")
#         pwd = input("Enter Your password:  ")

#         query = """
#                 SELECT user_id FROM
#                 users WHERE  email = %s and password = %s"""

#         cursor.execute(query,(email,pwd))

#         user_id = cursor.fetchone()

#         if user_id:
#             print("Login Successfull..")
#             print("User Id: ",user_id[0])
#             return True

#         else:
#             print("Email or Password is wrong..")
#             return False

#     except mysql.connector.Error as e:
#         print("Database error:", e)


# ADD STUDENT FUNCTION
def add_student():
    pass



# VIEW STUDENT FUNCTION
def view_student():
    pass


# SEARCH STUDENT FUNCTION
def search_student():
    pass


# UPDATE STUDENT FUNCTION
def updat_student():
    pass


# DELETE STUDENT FUNCTION
def delete_student():
    pass


# LOGOUT STUDENT FUNCTION
def logout_student():
    pass

# the student menu function

def student_menu(user_id):

    while True:
        print("\n"+ "=" *35)
        print(" STUDENT MANAGEMENT SYSTEM. ")
        print("="*35)
        print("1. Add Student.")
        print("2. View all student.")
        print("3. Search Student. ")
        print("4. Update Student.")
        print("5. Delete Student.")
        print("6. Logout.")
        print("7. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            updat_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            logout_student()

        elif choice == "7":
            print("Exit...")
            break

        else:
            print("INVALID OPTION SELECTED.")


# the register and the login menu:

while True:
    print("----Welcome to the Student Management System----")
    print("\n1. Register.")
    print("2. Login.")
    print("3. To Exit.")

    choice = input("Enter your choice: ")

    if choice == "1":
        user = user_register()
        if user:
            student_menu(user)

    elif choice == "2":
        user = user_login()
        if user:
            student_menu(user)
        

    elif choice == "3":
        print("Thank you..\nExit")
        break

    else:
        print("Invalid Option. ")


        
