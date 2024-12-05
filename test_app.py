from app import app

def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b"Hello, CI/CD!"

