from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String ,Float
Base =declarative_base()

class Student(Base):
    roll_no= Column
    name: str
    student_class: int
    age: int
    gender: str
    phone: str
