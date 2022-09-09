import unittest
from services.factorial import FactorialService
from starlette.testclient import TestClient
from server import app


class FactorialTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app=app)

    def test_factorial_calculation(self):
        fibonacci_service = FactorialService(n=20)
        fibonacci_result = fibonacci_service.calculate()
        assert fibonacci_result == 2432902008176640000

    def test_factorial_invalid_payload(self):
        response = self.client.post('/math/v1/factorial')
        assert response.status_code == 400
        response_payload = response.json()
        assert response_payload['message'][0]['code'] == 'E002'

    def test_factorial_invalid_method(self):
        response = self.client.get('/math/v1/factorial')
        assert response.status_code == 405

    def test_factorial_valid_payload(self):
        response = self.client.post('/math/v1/factorial', json={'n': 20})
        response_payload = response.json()
        assert response_payload['data']['result'] == 2432902008176640000

    def test_factorial_calculation_large(self):
        response = self.client.post('/math/v1/factorial', json={'n': 5000})
        response_payload = response.json()
        assert response_payload['message'][0]['code'] == 'E001'
