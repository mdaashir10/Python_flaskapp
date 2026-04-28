import pytest
from app import app

# Testing CI/CD pipelines

@pytest.fixture     # reuseable setup function
def client():
    app.testing = True
    return app.test_client()    # creates fake browser client

# Test functions
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_info(client):
    response = client.get('/info')
    assert response.status_code == 200
