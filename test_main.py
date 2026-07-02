from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    # Send a GET request to the home page
    response = client.get("/")
    
    # Assert that the server responds with a 200 OK status code
    assert response.status_code == 200
    
    # Assert that our key success message is present in the HTML output
    assert "CI/CD Test Application" in response.text