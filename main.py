from fastapi import FastAPI
from Database.models import Student
app =FastAPI()


@app.get("/")
def welcome():
    return "Welcome"

students=[
    Student(roll_no =1, name="Aniket srivastava",student_class=2, age= 14, gender= "Male", phone= "123456789")
]

@app.get("/students")
def get_students():
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