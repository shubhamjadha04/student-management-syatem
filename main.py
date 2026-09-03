from auth import admin_login,student_login
from student import(
    view_attendance,
    view_courses,
    view_marks,
    view_profile,
)
from admin import(
    add_student,
    add_course,
    delete_student,
    update_student,
    manage_attendance,
    add_teacher,
    reports,

)

# the admin menu function

def admin_menu():

    while True:
        print("\n" + "=" * 40)
        print("          ADMIN MENU")
        print("=" * 40)

        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Add Course")
        print("5. Add Teacher")
        print("6. Update Teacher")
        print("7. Delete Teacher")
        print("8. Assign Teacher")
        print("9. Enroll course")
        print("10. Logout")

        

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
            add_teacher()

        elif choice == "6":
            manage_attendance()

        elif choice == "7":
            reports()

        elif choice == "10  ":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")
            


# the student menu function

def student_menu(user_id):

    while True:

        print("\n" + "=" * 40)
        print("          STUDENT MENU")
        print("=" * 40)

        print("1. View Profile")
        print("2. View Courses")
        print("3. View Marks")
        print("4. View Attendance")
        print("5. Logout")

        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            view_profile(user_id)

        elif choice == "2":
            view_courses(user_id)

        elif choice == "3":
            view_marks(user_id)

        elif choice == "4":
            view_attendance(user_id)

        elif choice == "5":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


# the register and the login menu:

while True:
    print("----Welcome to the Student Management System----")
    print("\n1 Admin login.")
    print("2. Student Login.")
    print("3. To Exit.")

    choice = input("Enter your choice: ")

    if choice == "1":
        admin_id = admin_login()
        if admin_id:
            admin_menu()
 
    elif choice == "2":
        student_id = student_login()
        if student_id:
            student_menu(student_id)
   
    elif choice == "3":
        print("Thank you..\nExit")
        break

    else:
        print("Invalid Option. ")