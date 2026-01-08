from fastapi import FastAPI
from Database.models import Student
from Database.confiq import session, engine
from Database.models import db_models
app =FastAPI()

db_models .Base.metadata.create_all(bind=engine)


@app.get("/")
def welcome():
    return "Welcome"

students=[
    Student(roll_no =1, name="Aniket srivastava",student_class=11, age= 14, gender= "Male", phone= "123456789")
]

@app.get("/students")
def get_students():
    db= session()
    
    return students


@app.get("/student/{id}")
def get_student_id(id:int):
    for student in students:
        if student.id == id:
            return student
    
    return "Student Not Found"

@app.post("/student")
def add_student(student:Student):
    students.append(student)
    return student

@app.put("/student")
def update_student(id: int, student:Student):
    for i in range(len(students)):
        if students[i].id == id:
            students[i]=student
            return "Student Added"
    return "No student found"

@app.delete("/student")
def delete_student(id:int):
    for i in range(len(students)):
        if students[i].id == id:
            if students[i].id == id:
                del students[i]
                return "Student Deleted"
    return " No student Found"