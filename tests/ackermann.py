import unittest
from services.ackermann import AckermannService
from starlette.testclient import TestClient
from server import app


class AckermannTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app=app)

    def test_ackermann_calculation(self):
        ackermann_service = AckermannService(parameter_m=3, parameter_n=5)
        ackermann_result = ackermann_service.calculate()
        assert ackermann_result == 253

    def test_ackermann_invalid_payload(self):
        response = self.client.post('/math/v1/ackermann')
        assert response.status_code == 400
        response_payload = response.json()
        assert response_payload['message'][0]['code'] == 'E002'

    def test_ackermann_invalid_method(self):
        response = self.client.get('/math/v1/ackermann')
        assert response.status_code == 405

    def test_fibonacci_valid_payload(self):
        response = self.client.post('/math/v1/ackermann', json={'m': 3, 'n': 5})
        response_payload = response.json()
        assert response_payload['data']['result'] == 253

    def test_fibonacci_calculation_large(self):
        response = self.client.post('/math/v1/ackermann', json={'m': 5, 'n': 10})
        response_payload = response.json()
        assert response_payload['message'][0]['code'] == 'E001'
