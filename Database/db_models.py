from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String ,Float
Base =declarative_base()

class Student(Base):
    roll_no= Column(Integer,primary_key=True,Index=True)
    name = Column(String)
    student_class =Column(Integer)
    age= Column(Integer)
    gender= Column(String)
    phone = Column(String)
