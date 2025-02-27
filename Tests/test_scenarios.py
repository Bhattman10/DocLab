import requests
import json
import re

def parse_input(file, list_of_inputs):
    line = file.readline()
    while line and line.strip() != "---------------------------":
        list_of_inputs.append(line.strip())
        line = file.readline()
    return line

def parse_file_name(line, list_of_file_names):
    name_of_file = line.strip('-\n')
    if name_of_file:
        list_of_file_names.append(name_of_file)

def parse_file_contents(file, list_of_code_contents):
    code_contents = ""
    line = file.readline()
    while line and line.strip() != "---------------------------":
        code_contents += line
        line = file.readline()
    list_of_code_contents.append(code_contents)
    return line  # Return updated line

def parse(file_path):

    list_of_file_names = []
    list_of_code_contents = []
    list_of_inputs = []

    with open(file_path, 'r', encoding='utf-8') as file:
        line = file.readline()  # Read first line

        while line:
            print(line)
            if line.strip() == "-----------input-----------":
                line = parse_input(file, list_of_inputs)
            elif line == "\n":
                line = file.readline()
                continue
            else:
                parse_file_name(line, list_of_file_names)
                line = parse_file_contents(file, list_of_code_contents)
            line = file.readline()  # Read next line for next loop iteration

    print(list_of_file_names)
    print(list_of_code_contents)
    print(list_of_inputs)
    
    return list_of_file_names, list_of_code_contents, list_of_inputs

def client(data):

    url = "http://backend:5000/"

    try:
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def manager(file_path):
    list_of_file_names, list_of_code_contents, user_input = parse(file_path)
    data = {
        "document_id": "12345",
        "list_of_file_names" : list_of_file_names,
        "list_of_code_contents" : list_of_code_contents,
        "user_input" : user_input
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