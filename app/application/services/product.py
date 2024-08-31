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

   
