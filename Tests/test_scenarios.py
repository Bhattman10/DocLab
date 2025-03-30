import requests
import json
import textwrap


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
            if line.strip() == "-----------input-----------":
                line = parse_input(file, list_of_inputs)
            elif line == "\n":
                line = file.readline()
                continue
            else:
                parse_file_name(line, list_of_file_names)
                line = parse_file_contents(file, list_of_code_contents)
            line = file.readline()  # Read next line for next loop iteration

    return list_of_file_names, list_of_code_contents, list_of_inputs


def client(data):

    url = "http://127.0.0.1:5000/"

    try:
        response = requests.post(url, data=json.dumps(data), headers={
                                 'Content-Type': 'application/json'})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


def manager(file_path):
    list_of_file_names, list_of_code_contents, user_input = parse(file_path)
    data = {
        "document_id": "12345",
        "list_of_file_names": list_of_file_names,
        "list_of_code_contents": list_of_code_contents,
        "user_input": user_input
    }
    json_string = client(data)
    data = json.loads(json_string)
    return data["standard_output"], data["errors"]


def test_hello():
    standard_output, errors = manager("./Scenarios/hello.txt")
    assert standard_output == "Hello World!\n"
    assert errors == ""


def test_math():
    standard_output, errors = manager("./Scenarios/math.txt")
    assert standard_output == "3\n"
    assert errors == ""


def test_import():
    standard_output, errors = manager("./Scenarios/import.txt")
    assert standard_output == textwrap.dedent("""\
        Hello, Ethan!
        """)
    assert errors == ""


def test_input():
    standard_output, errors = manager("./Scenarios/input.txt")
    assert standard_output == textwrap.dedent("""\
        What is your name?
        Hello, Ethan!
        """)
    assert errors == ""


def test_multi_input():
    standard_output, errors = manager("./Scenarios/multi_input.txt")
    assert standard_output == textwrap.dedent("""\
        What is your first name?
        What is your last name?
        Hello, Ethan Bhatt!
        """)
    assert errors == ""


def test_calculator():
    standard_output, errors = manager("./Scenarios/calculator.txt")
    assert standard_output == textwrap.dedent("""\
        Select operation.
        1.Add
        2.Subtract
        3.Multiply
        4.Divide
        Enter choice(1/2/3/4): Enter first number: Enter second number: 2.0 + 2.0 = 4.0
        Let's do next calculation? (yes/no): """)
    assert errors == ""
