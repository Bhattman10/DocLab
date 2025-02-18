import requests
import json

def client(data):

    url = "http://backend:5000/"

    try:
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def test_hello():
    files = [["main.py", "print(\"Hello World!\")"]]
    data = {
        "session_id": "12345",
        "files" : files
    }
    assert client(data) == '{"result":"Hello World!\\n"}\n'

def test_addition():
    files = [["main.py", "print(1+2)"]]
    data = {
        "session_id": "12345",
        "files" : files
    }
    assert client(data) == '{"result":"3\\n"}\n'