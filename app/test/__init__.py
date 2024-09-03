from unittest.mock import Mock, patch
from app.domain.entities.lead import LeadEntityFactory
from app.domain.repositories.lead import LeadRepository
from app.test.data.lead import expected_leads_catalog, expected_lead_description


lead_data = {
    "fullname": "John Doe",
    "email": "johndoe1084@example.com",
    "address": "123 Main St, Springfield, IL",
    "phone": "+1-555-123-4567",
    "subject": "Computer Science",
    "course_time": "2024-09-02T09:00:00",
    "career": "Software Engineer",
    "inscription": "2024-09-01T12:00:00",
    "number_courses": 5
}
lead_repository_get_all = [lead_data for x in range(2)]
lead_repository_get_by_id = lead_data

@patch('app.infrastructure.repositories.adapters.sql_aclhemy.repositories.lead_repositories.LeadSQLAlchemyRepository', spec=True)
def create_mock_lead_repository(mock_repository: Mock):
    mock_lead_repo: LeadRepository = mock_repository.return_value
    mock_lead_repo.get_all = Mock(return_value=[LeadEntityFactory.create(**lead) for lead in lead_repository_get_all])
    mock_lead_repo.get_by_id = Mock(return_value=LeadEntityFactory.create(**lead_repository_get_by_id))
    mock_lead_repo.add = Mock(return_value=LeadEntityFactory.create(**lead_repository_get_by_id))
    mock_lead_repo.update = Mock(return_value=LeadEntityFactory.create(**lead_repository_get_by_id))
    return mock_lead_repo
