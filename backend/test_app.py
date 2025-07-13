import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_message(client):
    response = client.get('/api/message')
    assert response.status_code == 200
    assert b"Hello" in response.data
