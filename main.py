from auth import user_login,user_register
from student import(
    add_student,
    view_student,
    search_student,
    delete_student,
    update_student,
)
from admin import(
    add_student,
    add_course,
    delete_student,
    update_student,
    manage_attendance,
    manage_marks,
    reports,

)

# the admin menu function

def admin_menu(user_id):

    while True:
        print("\n" + "=" * 40)
        print("          ADMIN MENU")
        print("=" * 40)

        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Add Course")
        print("5. Manage Marks")
        print("6. Manage Attendance")
        print("7. Reports")
        print("8. Logout")

        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            update_student()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            add_course()

        elif choice == "5":
            manage_marks()

        elif choice == "6":
            manage_attendance()

        elif choice == "7":
            reports()

        elif choice == "8":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")
            


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
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("You have successfully logout..")
            break

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
        user_id , role = user
        if role == "admin":
            admin_menu(user_id)

        elif role == "student":
            student_menu(user_id)
            

    elif choice == "2":
        user = user_login()
        user_id,role = user

        if role == "admin":
            admin_menu(user_id)

        elif role == "student":
            student_menu(user_id)
        
    elif choice == "3":
        print("Thank you..\nExit")
        break

    else:
        print("Invalid Option. ")


        
