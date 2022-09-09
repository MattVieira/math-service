import unittest
from services.fibonacci import FibonnaciService
from starlette.testclient import TestClient
from server import app


class FibonnaciTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app=app)

    def test_fibonacci_calculation(self):
        fibonacci_service = FibonnaciService(n=10)
        fibonacci_result = fibonacci_service.calculate()
        assert fibonacci_result == 55

    def test_fibonacci_invalid_payload(self):
        response = self.client.post('/math/v1/fibonacci')
        assert response.status_code == 400
        response_payload = response.json()
        assert response_payload['message'][0]['code'] == 'E002'

    def test_fibonacci_invalid_method(self):
        response = self.client.get('/math/v1/fibonacci')
        assert response.status_code == 405

    def test_fibonacci_valid_payload(self):
        response = self.client.post('/math/v1/fibonacci', json={'n': 10})
        response_payload = response.json()
        assert response_payload['data']['result'] == 55

    def test_fibonacci_calculation_large(self):
        response = self.client.post('/math/v1/fibonacci', json={'n': 5000})
        response_payload = response.json()
        assert response_payload['message'][0]['code'] == 'E001'
