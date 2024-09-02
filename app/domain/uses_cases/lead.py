from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.lead import LeadEntity
from app.domain.events.lead import LeadCreatedEvent, LeadUpdatedEvent
from app.domain.repositories.lead import LeadRepository


class LeadUseCases(ABC):

    @abstractmethod
    def __init__(self, lead_repository: LeadRepository,
                 lead_created_event: LeadCreatedEvent,
                 lead_updated_event: LeadUpdatedEvent
                 ):
        self.lead_repository = lead_repository
        self.lead_created_event = lead_created_event
        self.lead_updated_event = lead_updated_event

    @abstractmethod
    def leads_catalog(self) -> List[LeadEntity]:
        raise NotImplemented
    @abstractmethod
    def lead_detail(self, id: int) -> LeadEntity:
        raise NotImplemented
    @abstractmethod
    def add_lead(self, lead: LeadEntity) -> LeadEntity:
        raise NotImplemented
    @abstractmethod
    def update_lead(self, product: LeadEntity) -> LeadEntity:
        raise NotImplemented