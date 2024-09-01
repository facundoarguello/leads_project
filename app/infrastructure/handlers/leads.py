from app.domain.entities.lead import LeadEntity
from app.infrastructure.adapters.sql_alchemy.database import get_db
from app.infrastructure.adapters.sql_alchemy.repositories.lead_repositories import LeadSQLAlchemyRepository
from app.infrastructure.events.lead import LeadCreatedQueueEvent, LeadUpdatedQueueEvent
from app.infrastructure.schemas.leads import LeadsOutput
from app.application.services.lead import LeadService
from fastapi import APIRouter, Depends
from app.infrastructure.container import container
from typing import List
router = APIRouter(
    prefix='/leads',
    tags=['leasds']
)


@router.get('/', response_model=List[LeadsOutput])

def read_root(lead_services: LeadService = Depends(lambda: container.lead_services)):
    response = lead_services.leads_catalog()
    return [lead.__dict__ for lead in response]
    