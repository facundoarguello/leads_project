from typing import List
from app.domain.uses_cases.lead import LeadUseCases
from app.domain.entities.lead import LeadEntity
from app.domain.events.lead import LeadCreatedEvent, LeadUpdatedEvent
from app.domain.repositories.lead import LeadRepository


class LeadService(LeadUseCases):

    

    def __init__(self, lead_repository: LeadRepository,
                 lead_created_event: LeadCreatedEvent,
                 lead_updated_event: LeadUpdatedEvent
                 ):
        super().__init__(lead_repository, lead_created_event, lead_updated_event)

    def leads_catalog(self) -> List[LeadEntity]:
        leads = self.lead_repository.get_all()
        return leads
    def lead_detail(self, id: int) -> LeadEntity:
        lead = self.lead_repository.get_by_id(id)
        return lead
    
    def add_lead(self, lead: LeadEntity) -> LeadEntity:
        product = self.lead_repository.add(lead)

        return product
    def update_lead(self, lead: LeadEntity) -> LeadEntity:
        lead = self.lead_repository.update(lead)
        return lead

   
