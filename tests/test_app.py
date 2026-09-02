from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Hello from Python Flask! CI/CD and Approval Gates are working." in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_message():
    client = app.test_client()

    response = client.get("/api/message")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Hello from Azure DevOps CI/CD!"