from app.domain.entities.lead import LeadEntityFactory
from app.infrastructure.events.lead import LeadCreatedQueueEvent, LeadUpdatedQueueEvent
from app.infrastructure.adapters.sql_alchemy.repositories.lead_repositories import LeadSQLAlchemyRepository
from app.application.services.lead import LeadService
from app.infrastructure.adapters.sql_alchemy.database import get_db

class Container:
    def __init__(self):
        # Factories
        self.lead_factory = LeadEntityFactory()

        # BD
        self.db_session = get_db()

        # Repositories
        self.lead_repository = LeadSQLAlchemyRepository(self.db_session)

        # Events
        self.lead_created_event = LeadCreatedQueueEvent()
        self.lead_updated_event = LeadUpdatedQueueEvent()

        # Services
        self.lead_services = LeadService(
            self.lead_repository,
            self.lead_created_event,
            self.lead_updated_event
        )

container = Container()