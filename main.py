from auth import user_login,user_register
from student import(
    add_student,
    view_student,
    search_student,
    delete_student,
    update_student,
)


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


        
