# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'OK'

def test_readings_endpoint(client):
    response = client.get('/api/v1/readings/latest')
    assert response.status_code == 200
    assert 'temperature_celsius' in response.json
