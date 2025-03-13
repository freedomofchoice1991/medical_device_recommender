import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ✅ Test home route
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

# ✅ Test recommendation API with a valid product code
def test_recommend_valid():
    response = client.get("/recommend/KNY")  # Replace with an actual product code in DB
    assert response.status_code == 200
    data = response.json()
    assert "strong_matches" in data
    assert "potential_alternatives" in data

# ✅ Test recommendation API with an invalid product code
def test_recommend_invalid():
    response = client.get("/recommend/INVALID_CODE")
    assert response.status_code == 200
    assert "error" in response.json()

# ✅ Test grouped API
def test_grouped():
    response = client.get("/grouped")
    assert response.status_code == 200
    assert "grouped_devices" in response.json()
