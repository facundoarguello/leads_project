import pytest
from app.application.services.lead import LeadService
from app.domain.entities.lead import LeadEntity, LeadEntityFactory
from app.infrastructure.container import container
from app.test import create_mock_lead_repository
from app.test.data.lead import expected_lead_description


class TestLeadService:

    """
    this fixture fulfills the function of dependency injection for all tests
    """
    @pytest.fixture(autouse=True)
    def injector(self):
        container = container
        with container.lead_repository.override(create_mock_lead_repository()):
            self.lead_service: LeadService = container.lead_services()
            self.lead_factory: LeadEntityFactory = container.lead_factory()

    def test_that_all_leads_in_the_catalog_are_an_entity(self):
        catalog = self.lead_service.leads_catalog()
        for lead in catalog:
            assert type(lead) is LeadEntity

    def test_that_lead_detail_is_an_entity(self):
        lead = self.lead_service.lead_detail('mock_id')
        assert type(lead) is LeadEntity

    def test_lead_name_is_correct(self):
        lead = self.lead_service.lead_detail('mock_id')
        assert lead.fullname == expected_lead_description['fullname']

    def test_register_lead(self):
        fullname, email, address, phone, subject, course_time, career, inscription, number_courses = expected_lead_description.values()
        lead_entity = self.lead_factory.create(None, fullname, address,email, phone, subject, course_time, career, inscription, number_courses)
        lead = self.lead_service.register_lead(lead_entity)
        assert type(lead) is LeadEntity
        assert lead.id == 1

    def test_update_lead(self):
        fullname, email, address, phone, subject, course_time, career, inscription, number_courses = expected_lead_description.values()
        lead_entity = self.lead_factory.create(None, fullname, address,email, phone, subject, course_time, career, inscription, number_courses)
        lead = self.lead_service.update_lead(lead_entity)
        assert type(lead) is LeadEntity
