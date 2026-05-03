from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_login():
    response = client.post("/auth/login")
    assert response.status_code == 200
    assert "token" in response.json()
    assert response.json()["token"] == "fake-jwt-token"
