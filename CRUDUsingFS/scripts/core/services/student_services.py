from fastapi import APIRouter
from scripts.core.Handler.handler_student import add_student,get_all_students,update_student,delete_student,send_item
from scripts.schema.studdent_schema import Student,Email
student_router = APIRouter()


# Insert a student
@student_router.post("/addStudent/")
def add(student: Student):
    return add_student(student)


# Get all students from Mongodb
@student_router.get("/getAllStudents")
def getStudent():
    return get_all_students()


# updating the student record
@student_router.put("/updateStudent/{std_id}")
def updateStd(std_id: int, student: Student):
    return update_student(std_id, student)


# Delete Student
@student_router.delete("/deleteStudentById/{std_id}")
def deleteStd(std_id: int):
    return delete_student(std_id)

    
# Send Mail
@student_router.post("/send_email")
def sendMail(email: Email):
    return send_item(email)


    