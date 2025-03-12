from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_ticket():
    response = client.post("/tickets/", json={"title": "Test Bug", "description": "API test", "status": "open"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Bug"

def test_get_tickets():
    response = client.get("/tickets/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

