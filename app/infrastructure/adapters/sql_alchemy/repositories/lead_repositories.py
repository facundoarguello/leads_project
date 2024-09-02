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
    
    def get_by_id(self, id: int):
        data_by_id : LeadDBModel | None  = self.session.get(LeadDBModel,id)
        
        create_lead : LeadEntity | None = LeadEntityFactory.create(
            id=data_by_id.id,fullname=data_by_id.fullname,
            email=data_by_id.email,
            address=data_by_id.address,
            phone=data_by_id.phone,
            subject=data_by_id.subject,
            course_time=data_by_id.course_time,
            career=data_by_id.career,
            inscription=data_by_id.inscription,
            number_courses=data_by_id.number_courses
        )
        return create_lead

    def add(self, lead: LeadEntity):
        model : LeadDBModel = LeadDBModel(fullname=lead.fullname,
        email=lead.email,
        address=lead.address,
        phone=lead.phone,
        subject=lead.subject,
        course_time=lead.course_time,
        career=lead.career,
        inscription=lead.inscription,
        number_courses=lead.number_courses)
        try:
           
            self.session.add(model)

            self.session.commit()
        
            self.session.refresh(model)
        
        except :
            self.session.rollback()
            raise
        lead.id = model.id
        
        return lead

    def update(self, lead: LeadEntity):
        lead_by_id = self.session.query(LeadDBModel).get(lead.id)
        for key, value in lead.__dict__.items():
            setattr(lead_by_id, key, value)

        try:
           
            self.session.commit()
            self.session.flush()
                    
        except :
            self.session.rollback()
            raise
        return lead