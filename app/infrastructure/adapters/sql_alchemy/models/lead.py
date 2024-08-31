from app.infrastructure.adapters.sql_alchemy.models.base_entity import BaseEntity
from sqlalchemy import Column, Integer, String, DateTime


class LeadDBModel(BaseEntity):
    __tablename__ = 'leads'
    fullname = Column(String, index=True)
    email = Column(String)
    address = Column(String)
    phone = Column(String)
    subject = Column(String)
    course_time = Column(Integer)
    career = Column(String)
    inscription = Column(DateTime)
    number_courses = Column(Integer)
