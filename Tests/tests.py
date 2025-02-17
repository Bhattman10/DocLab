import requests
import json

def frontend(data):

    url = 'http://127.0.0.1:5000/'
    headers = {'Content-type': 'application/json'}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except json.JSONDecodeError:
        print("Invalid JSON response received")

def test_hello():
    files = ["main.py", "print(\"Hello World!\")"]
    data = {'session_id' : '12345', 'files': files}
    assert frontend(data) == 1
