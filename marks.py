from database import cursor,conn
import mysql.connector
from auth import(
    validate_email,
    email_exists,
)

from teacher import (
    view_enrolled_students,
)


def add_marks(user_id):
    view_enrolled_students()

add_marks(13)




def update_marks(user_id):
    pass

def view_marks(user_id):
    pass