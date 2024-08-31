from pydantic import BaseModel,  EmailStr, Field
from datetime import datetime


class LeadsInput(BaseModel):
    fullname: str
    email: EmailStr | None = Field(default=None)
    address: str
    phone: str
    subject: str
    course_time: int 
    career: str
    inscription: datetime
    number_courses: int

class LeadsOutput(BaseModel):
    id: int
    fullname: str
    email: EmailStr | None = Field(default=None)
    address: str
    phone: str
    subject: str
    course_time: int 
    career: str
    inscription: datetime
    number_courses: int
    updated: datetime