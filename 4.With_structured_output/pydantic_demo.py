from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Swayam"
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: float = Field(gt=0, lt=10)

new_student = {"age": 22, "email": "xyz@gmail.com", 'cgpa': 8.8}

student = Student(**new_student)
print(student)

student_dict = dict(student)
print(student_dict)

student_json = student.model_dump_json()
print(student_json)