import requests
import json
import re

def parse(file_path):

    list_of_file_names = []
    list_of_code_contents = []
    code_contents = ""

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line == "---------------------------\n" or line == "---------------------------":
                list_of_code_contents.append(code_contents)
                code_contents = ""
            elif line[:10] == "----------":
                file_name = ""
                for char in line[10:]:
                    if char != '-' and char != '\n':
                        file_name += char
                if file_name != '\n' and file_name != '':
                    list_of_file_names.append(file_name)
            else:
                code_contents += line
    
    return list_of_file_names, list_of_code_contents

def client(data):

    url = "http://backend:5000/"

    try:
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def manager(file_path):
    list_of_file_names, list_of_code_contents = parse(file_path)
    data = {
        "document_id": "12345",
        "list_of_file_names" : list_of_file_names,
        "list_of_code_contents" : list_of_code_contents
    }
    json_string = client(data)
    data = json.loads(json_string)
    return data["result"]

def test_hello():
    result = manager("./Scenarios/hello.txt")
    assert result == "Hello World!\n"

def test_math():
    result = manager("./Scenarios/math.txt")
    assert result == "3\n"

def test_import():
    result = manager("./Scenarios/import.txt")
    assert result == "Hello, Ethan!\n"

def test_input():
    result = manager("./Scenarios/input.txt")
    assert result == "Hello, Ethan!\n"