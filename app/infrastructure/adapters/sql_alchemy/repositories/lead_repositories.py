from sqlalchemy.orm import Session
from typing import List
from app.domain.entities.lead import LeadEntityFactory, LeadEntity
from app.domain.repositories.lead import LeadRepository
from app.infrastructure.adapters.sql_alchemy.models.lead import LeadDBModel


class LeadSQLAlchemyRepository(LeadRepository):

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[LeadEntity]:
        return [LeadEntityFactory.create(**lead) for lead in self.session.query(LeadDBModel).all()]