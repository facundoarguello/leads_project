from app.domain.entities.lead import LeadEntity, LeadEntityFactory
from app.infrastructure.schemas.leads import LeadResponse, LeadsInput, LeadsOutput, Meta
from app.application.services.lead import LeadService
from fastapi import APIRouter, Depends
from app.infrastructure.container import container
from typing import List
router = APIRouter(
    prefix='/leads',
    tags=['leads']
)


@router.get('/', response_model=LeadResponse)
def read_root(lead_services: LeadService = Depends(lambda: container.lead_services)):
    leads = lead_services.leads_catalog()
    response = LeadResponse(
        meta=Meta(
            total_elements=len(leads),
            total_pages=1,
            current_page=1
        ),
        data=[lead.__dict__ for lead in leads]
    )
    return response

@router.get('/{id}', response_model=LeadResponse)
def get_description(id: int, product_services: LeadService = Depends(lambda: container.lead_services)) -> dict:
    lead : LeadEntity | None = product_services.lead_detail(id)
    response = LeadResponse(
        data=lead.__dict__  
    )
    return response

@router.post('/', response_model=LeadResponse)
def post_lead(
        lead: LeadsInput,
        lead_factory: LeadEntityFactory = Depends(lambda: container.lead_factory),
        lead_services: LeadService = Depends(lambda: container.lead_services)
) -> dict:
    fullname, email, address, phone, subject, course_time, career, inscription, number_courses = lead.__dict__.values()
    lead_entity: LeadEntity = lead_factory.create(None, fullname, address,email, phone, subject, course_time, career, inscription, number_courses)
    lead_entity_then_added: LeadEntity  =  lead_services.add_lead(lead_entity)
    response = LeadResponse(
        data=lead_entity_then_added.__dict__
    )
    
    return response
    
@router.put('/{id}', response_model=LeadResponse)
def update_lead(
        id: int,
        lead: LeadsInput,
        lead_factory: LeadEntityFactory = Depends(lambda: container.lead_factory),
        lead_services: LeadService = Depends(lambda: container.lead_services)
) -> dict:
    fullname, email, address, phone, subject, course_time, career, inscription, number_courses = lead.__dict__.values()
    lead_entity: LeadEntity = lead_factory.create(id, fullname, address,email, phone, subject, course_time, career, inscription, number_courses)
    lead_entity_then_updated: LeadEntity  =  lead_services.update_lead(lead_entity)
    response = LeadResponse(
        data=lead_entity_then_updated.__dict__
    )
    return response