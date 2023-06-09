from scripts.schema.studdent_schema import Student
from scripts.utilities.mongodb import Mongo
from scripts.schema.studdent_schema import Email
from scripts.core.Handler.mail_handler import send_email

# def add_student(self, input_details):
#     try:
#         # All Logic here
#         print(input_details)
#         res = self.mongo_obj.insert_record(input_details)

#         if res:

#             return {"message": "Student added successfully", "status": "success"}
#         else:
#             return {'message': "", "status": "failed"}
#     except Exception as e:
#         # Log the exception
#         return {'message': "", "status": "failed", "error": str(e)}
obj = Mongo()


def add_student(student: Student):
    student_dict = student.dict()
    result = obj.myDB.insert_one(student_dict)
    return {"id": "Student added successfully"}


def get_all_students():
    students = obj.myDB.find({})
    details = []
    for document in students:
        detail = {'id': document['id'], 'name': document['name'], 'address': document['address']}
        details.append(detail)
    return {"details": details}

def update_student(std_id: int, student: Student):
    result = obj.myDB.update_one({"id": std_id}, {"$set": student.dict()})
    if result.modified_count == 1:
        return {"message": "Student updated successfully"}
    else:
        return {"error": "Student not found"}
    

def delete_student(std_id: int):
    try:
        obj.myDB.delete_one({"id": std_id})
        return {"message": "Student deleted successfully"}
    except Exception as e:
        return {"error": "Student not found"}
    
def send_item(email: Email):
    return send_email(email)