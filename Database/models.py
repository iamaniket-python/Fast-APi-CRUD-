from pydantic import BaseModel

class Student(BaseModel):
    roll_no: int
    name: str
    student_class: int
    age: int
    gender: str
    phone: str
