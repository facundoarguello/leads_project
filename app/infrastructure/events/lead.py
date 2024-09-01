from app.domain.entities.lead import LeadEntity
from app.domain.events.lead import LeadCreatedEvent, LeadUpdatedEvent


class LeadCreatedQueueEvent(LeadCreatedEvent):

    def send(self, lead: LeadEntity):
        # TODO: Your code here
        return True

class LeadUpdatedQueueEvent(LeadUpdatedEvent):

    def send(self, lead: LeadEntity):
        # TODO: Your code here
        return True
