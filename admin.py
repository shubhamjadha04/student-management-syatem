from database import cursor,conn
import mysql.connector
from auth import(
    validate_email,
    email_exists,
)

# adding all details of the student in students table
def add_student_detail(user_id):
    roll_no = input("Enter Roll no.: ")
    phone = input("Enter phone no.: ")
    address = input("Enter address: ")
    gender = input("Enter gender: ")
    dob = input("Enter date of birth: ")
    branch = input("Enter Branch: ")
    add_year =  input("Enter addimission year: ")


    query = """
              INSERT INTO students(user_id,roll_no,phone,address, gender, dob, branch, admission_year)
              VALUES(%s,%s,%s,%s,%s,%s,%s,%s)  
                """

    cursor.execute(query,(user_id,roll_no,phone,address,gender,dob,branch,add_year))
    conn.commit()
    print("The details addes successfully.")


# this is the admin menu 

def add_student():
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
                    INSERT INTO users(name,email,password,role)
                    VALUES(%s,%s,%s,%s)
                """
        cursor.execute(query,(name,email,pwd,'student'))
        conn.commit()

        user_id = cursor.lastrowid
        print("Student added Successfully..\n add other details.")
        add_student_detail(user_id)
        
        
# exception handling
    except ValueError as e:
        print("Error",e)
        return None

    except mysql.connector.Error as e:
        print("Error",e)
        return None
  
# view all student from the users table

def view_all_students():
    query = """
        SELECT user_id, name, email
        FROM users
        WHERE role = 'student'
    """

    cursor.execute(query)
    students = cursor.fetchall()

    print("\n========== ALL STUDENTS ==========")
    print(f"{'ID':<10}{'NAME':<20}{'EMAIL':<30}")
    print("-" * 60)

    for student in students:
        print(f"{student[0]:<10}{student[1]:<20}{student[2]:<30}")

    print("=" * 60)


# update_student function 

def update_student():
    try:
        view_all_students()

        user_id = input("Enter the id of the student want to update: ")
        # checking the student is present
        check_query = """
            SELECT user_id
            FROM students
            WHERE user_id = %s
        """

        cursor.execute(check_query, (user_id,))
        student = cursor.fetchone()

        if student is None:
            print("Student ID not found.")
            return


        roll_no = input("Enter Roll no.: ")
        phone = input("Enter phone no.: ")
        address = input("Enter address: ")
        gender = input("Enter gender: ")
        dob = input("Enter date of birth: ")
        branch = input("Enter Branch: ")
        add_year =  input("Enter addimission year: ")
        
        
        query = """
                    UPDATE students 
                    SET roll_no = %s,
                        phone = %s,
                        address = %s,
                        gender= %s,
                        dob =%s,
                        branch = %s,
                        admission_year = %s

                    WHERE user_id = %s 
                        """
        
        cursor.execute(query,(roll_no,phone,address,gender,dob,branch,add_year,user_id))
        conn.commit()
        print("The Student details updated successfully.")

    except mysql.connector.Error as e:
        print("Error",e)
        

# DELETE STUDENT FUNCTION
def delete_student():
    try:      
        view_all_students()

        user_id = input("Enter Id of the student which you want to delete: ")
        query1 = """
                    DELETE FROM students 
                    WHERE user_id = %s"""

        query2 = """
                        DELETE FROM  users
                        WHERE user_id = %s"""

    

        cursor.execute(query1,(user_id,))

        
        if cursor.rowcount == 0:
            print("Student not found.")
            conn.rollback()
            return

        cursor.execute(query2,(user_id,))
        conn.commit()

        print("The student deleted successfully..")

    except mysql.connector.Error as e:
        print("Error",e)
    
# add add_course function
def add_course():
    try:
        course_name = input("Enter the course name: ")
        course_code = input("Enter the course code: ")

        # checking course code 
        check_code = """SELECT course_name 
                        FROM courses WHERE
                        course_code = %s"""
        cursor.execute(check_code,(course_code,))
        check = cursor.fetchone()

        if check:
            print("course code alrady exists.")
            return

        credits = int(input("Enter the credits: "))

        if credits < 0:
            raise ValueError("Credits must be greater than 0.")

        query = """
                   INSERT INTO courses(course_name,course_code,credits)
                   VALUES(%s,%s,%s)                     
                """

        cursor.execute(query,(course_name,course_code,credits))
        conn.commit()

        print("The course added succeffully..")


    except ValueError:
        print("The credits must be numbers.")

    except mysql.connector.Error as e:
        conn.rollback()
        print("Error",e)



# ADD TEACHER EXTRA INFO
def teacher_info(user_id):
    teacher_name = input("Enter the name of the teacher: ")
    phone = input("Enter the phone no: ")
    branch = input("Enter the branch: ")
    
    teach_query = """
                            INSERT INTO teachers(user_id,teacher_name,phone,branch)
                            VALUES(%s,%s,%s,%s)"""
    
    cursor.execute(teach_query,(user_id,teacher_name,phone,branch))
    conn.commit()
    
    t_id = cursor.lastrowid
    print("Teacher detail added successfully teacher_id is",t_id)

# add teacher function
def add_teacher():
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
                        INSERT INTO users(name,email,password,role)
                        VALUES(%s,%s,%s,%s)
                    """
        cursor.execute(query,(name,email,pwd,'teacher'))
        conn.commit()
    
        user_id = cursor.lastrowid
        print("Student added Successfully..\n add other details.")
        teacher_info(user_id)

            
            
    # exception handling
    except ValueError as e:
        print("Error",e)
        return None
    
    except mysql.connector.Error as e:
        print("Error",e)
        return None

#  VIEW ALL TEACHER FUNCTION
def view_all_teachers():
    query = """
        SELECT teacher_id, teacher_name,branch
        FROM teachers
    """

    cursor.execute(query)
    teachers = cursor.fetchall()

    print("\n========== ALL TEACHERS ==========")
    print(f"{'ID':<10}{'NAME':<20}{'BRANCH':<20}")
    print("-" * 60)

    for teacher in teachers:
        print(f"{teacher[0]:<10}{teacher[1]:<20}{teacher[2]:<20}")

    print("=" * 60)



    
# UPDATE TEACHER FUNCTION
def update_teacher():
    try:
        view_all_teachers()

        user_id = input("Enter the ID of the teacher you want to update: ")

        # Check whether teacher exists
        check_query = """
            SELECT teacher_id
            FROM teachers
            WHERE user_id = %s
        """

        cursor.execute(check_query, (user_id,))
        teacher = cursor.fetchone()

        if teacher is None:
            print("Teacher ID not found.")
            return

        teacher_name = input("Enter the name of the teacher: ")
        phone = input("Enter phone no.: ")
        branch = input("Enter Branch: ")

        query = """
            UPDATE teachers
            SET teacher_name = %s,
                phone = %s,
                branch = %s
            WHERE user_id = %s
        """

        cursor.execute(
            query,
            (teacher_name, phone, branch, user_id)
        )

        conn.commit()

        print("The teacher details updated successfully.")

    except mysql.connector.Error as e:
        print("Error:", e)



# DELETE TEACHER FUNCTION

def delete_teacher():
    try:      
        view_all_teachers()

        user_id = input("Enter Id of the Teacher which you want to delete: ")
        query1 = """
                    DELETE FROM teachers 
                    WHERE user_id = %s"""

        query2 = """
                        DELETE FROM  users
                        WHERE user_id = %s"""

    

        cursor.execute(query1,(user_id,))

        
        if cursor.rowcount == 0:
            print("Teacher not found.")
            conn.rollback()
            return

        cursor.execute(query2,(user_id,))
        conn.commit()

        print("The teacher deleted successfully..")

    except mysql.connector.Error as e:
        print("Error",e)


#checking all the courses
def show_course():
    query = """
             SELECT course_id, course_name,course_code, credits
             FROM courses                   
            """ 
    cursor.execute(query,())
    courses= cursor.fetchall()
    print("\n========== ALL COURSES ==========")
    print(f"{'ID':<10}{'NAME':<20}{'COURSE_CODE':<30}{'CREDITS':<20}")
    print("-" * 60)
    
    for course in courses:
        print(f"{course[0]:<10}{course[1]:<20}{course[2]:<30}{course[3]:<20}")
    
    print("=" * 60)



# teacher assign function 
def assign_teacher():
    try:
        view_all_teachers()

        teacher_id = input("Enter the teacher id: ")

        show_course()

        course_id = input("Enter the course id: ")

         # Check teacher exists
        query = """
            SELECT teacher_id
            FROM teachers
            WHERE teacher_id = %s
        """

        cursor.execute(query, (teacher_id,))
        teacher = cursor.fetchone()

        if not teacher:
            print("Teacher does not exist.")
            return

         # Check course exists
        query = """
            SELECT course_id
            FROM courses
            WHERE course_id = %s
        """

        cursor.execute(query, (course_id,))
        course = cursor.fetchone()

        if not course:
            print("Course does not exist.")
            return

        # check weather the course is assigned or not 
        query = """
            SELECT teacher_id
            FROM teacher_course
            WHERE teacher_id = %s AND course_id = %s
        """

        cursor.execute(query, (teacher_id, course_id))
        assignment = cursor.fetchone()

        if assignment:
            print("This teacher is already assigned to this course.")
            return

        query = """
                    INSERT INTO teacher_course(teacher_id,course_id)
                    VALUES(%s,%s)"""

        cursor.execute(query,(teacher_id,course_id))
        conn.commit()

        print("The course is assigned successfully.")



    except mysql.connector.Error as e:
        conn.rollback()
        print("Error",e)

    except validate_email:
        print("Invalid teacher_id or course_id..")
        

        

