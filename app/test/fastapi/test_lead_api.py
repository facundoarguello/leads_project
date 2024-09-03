import pytest
from app.infrastructure.fast_api import create_app
from fastapi.testclient import TestClient
from app.test import create_mock_lead_repository, expected_leads_catalog, expected_lead_description


class TestUserApi:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = create_app()
        self.client = TestClient(self.app)
        self.base_path = '/leads'

    def test_get_lead_catalog(self):
        with self.app.container.lead_repository.override(create_mock_lead_repository()):
            response = self.client.get(self.base_path + '/')
            assert expected_leads_catalog == response.json()
            assert response.status_code == 200

    def test_get_lead_detail(self):
        with self.app.container.lead_repository.override(create_mock_lead_repository()):
            response = self.client.get(self.base_path + '/mock_id')
            assert expected_lead_description == response.json()
            assert response.status_code == 200

    def test_post_register_lead(self):
        with self.app.container.lead_repository.override(create_mock_lead_repository()):
            response = self.client.post(
                self.base_path,
                json=expected_lead_description
            )
            assert expected_lead_description == response.json()
            assert response.status_code == 200

    def test_put_update_lead(self):
        with self.app.container.lead_repository.override(create_mock_lead_repository()):
            response = self.client.put(
                self.base_path + '/mock_id',
                json=expected_lead_description
            )
            assert expected_lead_description == response.json()
            assert response.status_code == 200