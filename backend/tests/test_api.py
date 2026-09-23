from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_overview():
    response = client.get("/api/overview")
    assert response.status_code == 200
    assert response.json()["completion_rate"] > 0
