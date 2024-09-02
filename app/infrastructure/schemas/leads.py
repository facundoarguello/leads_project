from pydantic import BaseModel,  EmailStr, Field
from typing import Any, List, Optional, Union
from datetime import datetime

class Meta(BaseModel):
    total_elements: Optional[int] = None
    total_pages: Optional[int] = None
    current_page: Optional[int] = None

class LeadsInput(BaseModel):
    fullname: str
    email: EmailStr | None = Field(default=None)
    address: str
    phone: str
    subject: str
    course_time: datetime 
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
    course_time: datetime 
    career: str
    inscription: datetime
    number_courses: int
    
class LeadResponse(BaseModel):
    meta: Meta = None
    data: Union[List[LeadsOutput], LeadsOutput] 