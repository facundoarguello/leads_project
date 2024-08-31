from app.infrastructure.schemas.leads import LeadsOutput
from fastapi import APIRouter
from typing import List
router = APIRouter(
    prefix='/leads',
    tags=['leasds']
)


@router.get('/', response_model=List[LeadsOutput])
def read_root():
    return [{
    "id": 1,
    "fullname": "John Doe",
    "email": "johndoe@example.com",
    "address": "123 Main St",
    "phone": "555-555-5555",
    "subject": "Computer Science",
    "course_time": 120,
    "career": "Software Engineer",
    "inscription": "2023-12-31T23:59:59",
    "number_courses": 3,
    "updated": "2024-01-01T00:00:00"
}]