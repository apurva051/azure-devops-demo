
from app import app


def test_homepage_loads():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")

        assert response.status_code == 200
        assert b"DevOps Project Dashboard" in response.data


def test_health_endpoint():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/health")

        assert response.status_code == 200

        data = response.get_json()

        assert data["status"] == "healthy"
        assert data["message"] == (
            "Application is running successfully"
        )


def test_unknown_route():
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/unknown-page")

        assert response.status_code == 404
