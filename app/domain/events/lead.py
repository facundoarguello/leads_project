from abc import ABC, abstractmethod
from app.domain.entities.lead import LeadEntity

class LeadCreatedEvent(ABC):

    @abstractmethod
    def send(self, lead: LeadEntity) -> bool:
        raise NotImplemented

class LeadUpdatedEvent(ABC):

    @abstractmethod
    def send(self, lead: LeadEntity) -> bool:
        raise NotImplemented
