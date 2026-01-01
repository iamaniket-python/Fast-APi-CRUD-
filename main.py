from fastapi import FastAPI
from Database.models import Student
app =FastAPI()


@app.get("/")
def welcome():
    return "Welcome"

students=[
    Student(roll_no =1, name="Aniket srivastava",student_class=11, age= 14, gender= "Male", phone= "123456789")
]

@app.get("/students")
def get_students():
    return students
