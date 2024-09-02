from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.lead import LeadEntity


class LeadRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[LeadEntity]:
        raise NotImplemented

    @abstractmethod
    def get_by_id(self, id: int) -> LeadEntity:
        raise NotImplemented

    @abstractmethod
    def add(self, lead: LeadEntity) -> LeadEntity:
        raise NotImplemented

    @abstractmethod
    def update(self, lead: LeadEntity) -> LeadEntity:
        raise NotImplemented