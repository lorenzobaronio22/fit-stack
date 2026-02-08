import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Fixture providing a TestClient for the FastAPI app."""
    return TestClient(app)


class TestRootEndpoint:
    """Test suite for the root endpoint."""

    def test_root_returns_200(self, client):
        """Test that root endpoint returns 200 OK status code."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_returns_hello_world_message(self, client):
        """Test that root endpoint returns correct message."""
        response = client.get("/")
        assert response.json() == {"message": "Hello World!"}

    def test_root_response_is_json(self, client):
        """Test that root endpoint returns JSON response."""
        response = client.get("/")
        assert response.headers["content-type"] == "application/json"

    def test_root_message_field_exists(self, client):
        """Test that response contains message field."""
        response = client.get("/")
        data = response.json()
        assert "message" in data
        assert isinstance(data["message"], str)
