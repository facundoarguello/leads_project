from sqlalchemy.orm import Session
from typing import List
from app.domain.entities.lead import LeadEntityFactory, LeadEntity
from app.domain.repositories.lead import LeadRepository
from app.infrastructure.adapters.sql_alchemy.models.lead import LeadDBModel


class LeadSQLAlchemyRepository(LeadRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[LeadEntity]:
        
        return [LeadEntityFactory.create(id=lead.id,fullname=lead.fullname,
            email=lead.email,
            address=lead.address,
            phone=lead.phone,
            subject=lead.subject,
            course_time=lead.course_time,
            career=lead.career,
            inscription=lead.inscription,
            number_courses=lead.number_courses,
            ) for lead in self.session.query(LeadDBModel).all()]
    
    def get_by_id(self, id: str):
        pass

    def add(self, lead: LeadEntity):
        pass

    def update(self, lead: LeadEntity):
        pass