import requests
import json

url = "http://flask:5000/"

files = [["main.py", "print(\"Hello World!\")"]]
data = {
    "session_id": "12345",
    "files" : files
}

try:
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    
    print("Request successful")
    print("Response status code:", response.status_code)
    print("Response text:", response.text)
    
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
