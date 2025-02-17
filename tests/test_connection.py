import sys
sys.path.append("/")
from connection import app
#Testing connection is open
client = app.test_client();
def test_connection():
    response = client.get('/')
    print(response.text)
    assert response.text == "flask is running!" 